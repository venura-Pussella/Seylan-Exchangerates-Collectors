from azure.storage.blob import BlobServiceClient
# from src.configuration.configuration import connect_str, container_name_blob
from dotenv import load_dotenv
import os

load_dotenv()

connect_str = os.getenv('connect_str')
container_name_blob = os.getenv('container_name_blob')

def upload_to_blob(csv_data, base_file_name):
    
    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    def get_next_file_name(base_name, index):
        return f"{base_name}_{index}.csv"
    
    def split_data_into_chunks(data, chunk_size=1400):
        lines = data.strip().split('\n')
        header = lines[0]
        chunks = [lines[i:i + chunk_size] for i in range(1, len(lines), chunk_size)]
        return header, [header + '\n' + '\n'.join(chunk) for chunk in chunks]
    
    # Split the incoming CSV data into chunks
    header, chunks = split_data_into_chunks(csv_data)
    index = 1
    
    for chunk in chunks:
        while True:
            file_name = get_next_file_name(base_file_name, index)
            blob_client = blob_service_client.get_blob_client(container=container_name_blob, blob=file_name)
            
            try:
                existing_data = blob_client.download_blob().readall().decode('utf-8')
                existing_lines = existing_data.strip().split('\n')
                line_count = len(existing_lines) - 1  # Subtract one for the header line
                
                if line_count < 1400:
                    # Combine existing data with the new chunk data
                    new_lines = chunk.strip().split('\n')[1:]  # Skip the header of the new chunk
                    combined_lines = existing_lines + new_lines
                    combined_data = '\n'.join(combined_lines)
                    
                    # Check if combined data exceeds 1400 rows
                    if len(combined_lines) <= 1400:
                        blob_client.upload_blob(combined_data.encode('utf-8'), overwrite=True)
                        break
                    else:
                        # Split the combined data to fit into the current file and prepare the overflow for the next file
                        remaining_lines = combined_lines[1400:]
                        chunk = header + '\n' + '\n'.join(remaining_lines)
                        combined_lines = combined_lines[:1400]
                        combined_data = '\n'.join(combined_lines)
                        blob_client.upload_blob(combined_data.encode('utf-8'), overwrite=True)
                        index += 1
                        continue
            except Exception as e:
                if "BlobNotFound" in str(e):
                    blob_client.upload_blob(chunk.encode('utf-8'))
                    break
                else:
                    # logger.error(f"Error while uploading: {e}")
                    raise
            index += 1



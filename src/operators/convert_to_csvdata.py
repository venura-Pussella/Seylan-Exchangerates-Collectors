import io
import csv

def write_exchange_rates_to_csv_data(exchange_rates_df):
    
    # Create an in-memory string buffer
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)

    # Write the header with the new 'Date', 'Time', and 'Bank' and ST_BANK_CODE columns
    writer.writerow([
        "Currency_Name",
        "Currency_Code",
        "Currency_Notes_Buying_Rate", 
        "Currency_Notes_Selling_Rate", 
        "Travelers_Cheques/Drafts_Buying_Rate", 
        "Travelers_Cheques/Drafts_Selling_Rate",
        "Telegraphic_Transfers_Buying_Rate",
        "Telegraphic_Transfers_Selling_Rate",
        "Import_Bills_Selling"
        "Bank", 
        "Date", 
        "Time", 
        "ST BANK CODE",
    ])

    # Write the data rows
    for index, row in exchange_rates_df.iterrows():
        writer.writerow(row)

    # Get the CSV data as a string
    csv_data = csv_buffer.getvalue()
    csv_buffer.close()
    
    return csv_data
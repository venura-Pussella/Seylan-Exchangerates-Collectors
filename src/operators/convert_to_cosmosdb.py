import uuid
def convert_df_to_cosmos_db_format(df):
    
    cosmos_db_documents = []
    for _, row in df.iterrows():
        rate_document = {
            "id": str(uuid.uuid4()),
            "timestamp": f"{row['Date']}T{row['Time']}Z",
            "currency_type": row['Currency_Name'],
            "code": row['Currency_Code'],
            "currency_notes_buying_rate": float(row['Currency_Notes_Buying']) if row['Currency_Notes_Buying'] else None,
            "currency_notes_selling_rate": float(row['Currency_Notes_Selling']) if row['Currency_Notes_Selling'] else None,
            "travelers_cheques_drafts_buying_rate": float(row['Travelers_Cheques/Drafts_Buying_Rate']) if row['Travelers_Cheques/Drafts_Buying_Rate'] else None,
            "travelers_cheques_drafts_selling_rate": float(row['Travelers_Cheques/Drafts_Selling_Rate']) if row['Travelers_Cheques/Drafts_Selling_Rate'] else None,
            "telegraphic_transfers_buying_rate": float(row['Telegraphic_Transfers_Buying_Rate']) if row['Telegraphic_Transfers_Buying_Rate'] else None,
            "telegraphic_transfers_selling_rate": float(row['Telegraphic_Transfers_Selling_Rate']) if row['Telegraphic_Transfers_Selling_Rate'] else None,
            "import_bills_selling":float(row['Import_Bills_Selling'])if row['Import_Bills_Selling'] else None,
            "bank": row['Bank'],
            "st_bank_code": row['ST BANK CODE']
        }
        cosmos_db_documents.append(rate_document)
    
    return cosmos_db_documents
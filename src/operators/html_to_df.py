import pandas as pd
from io import StringIO
from datetime import datetime

def process_html_content(html_content):
    html_file_like = StringIO(html_content)
    df = pd.read_html(html_file_like)[0]

    df.columns = ['_'.join(col).strip() for col in df.columns.values]
    # Reset the index of the DataFrame
    df1 = df.reset_index()
    # Drop the first column of the DataFrame
    df_dropped = df1.drop(df1.columns[[0, -1]], axis=1)
    df_dropped.columns = ['Currency_Name', 'Currency_Code', 'Currency_Notes_Buying','Currency_Notes_Selling',
                          'Travelers_Cheques/Drafts_Buying_Rate','Travelers_Cheques/Drafts_Selling_Rate',
                          'Telegraphic_Transfers_Buying_Rate','Telegraphic_Transfers_Selling_Rate','Import_Bills_Selling']
    
    df_dropped = df_dropped.fillna(0)

    df_dropped['Bank'] = 'Seylan'
    df_dropped['Date'] = datetime.now().strftime('%Y-%m-%d') # today's date 
    df_dropped['Time'] = datetime.now().strftime('%H:%M:%S') # today's time
    df_dropped['ST BANK CODE'] = '7287'

    
    return df_dropped

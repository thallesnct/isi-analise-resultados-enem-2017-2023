import pandas as pd

def convert_csv_to_xlsx(csv_file, xlsx_file, encoding='utf-8', delimiter=';', sheet_name='Sheet1'):
    """
    Converts a Brazilian Portuguese CSV file to an XLSX file.
    
    Parameters:
        csv_file (str): Path to the input CSV file.
        xlsx_file (str): Path to save the output XLSX file.
        encoding (str): Encoding of the CSV file. Defaults to 'utf-8'.
        delimiter (str): Delimiter used in the CSV file. Defaults to ';'.
        sheet_name (str): Name of the sheet in the Excel file. Defaults to 'Sheet1'.
    """
    try:
        chunk_size = 1_000_000  # Define the chunk size (less than Excel's row limit)
        df_chunks = pd.read_csv(csv_file, encoding=encoding, delimiter=delimiter, chunksize=chunk_size)
        
        for i, chunk in enumerate(df_chunks):
            with pd.ExcelWriter(f'{xlsx_file}-chunk-{i}.xlsx', engine='openpyxl') as writer:
                chunk.to_excel(writer, index=False, sheet_name=sheet_name)
                print(f"Chunk {i + 1} written to {xlsx_file}-chunk-{i}.xlsx")
        
        print(f"File successfully converted to {xlsx_file}-chunk-{i}.xlsx")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    csv_files = ["MICRODADOS_ENEM_2023_FILTRADOS", "MICRODADOS_ENEM_2022_FILTRADOS", "MICRODADOS_ENEM_2021_FILTRADOS", "MICRODADOS_ENEM_2020_FILTRADOS", "MICRODADOS_ENEM_2019_FILTRADOS", "MICRODADOS_ENEM_2018_FILTRADOS", "MICRODADOS_ENEM_2017_FILTRADOS"]
    
    for file_name in csv_files:
        
        csv_path = f"{file_name}.csv"  # Input CSV file
        xlsx_path = f"{file_name}"  # Output XLSX file
        convert_csv_to_xlsx(csv_path, xlsx_path)
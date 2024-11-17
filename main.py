import pandas as pd

def filter_csv_br(input_file, output_file):
    # Load the CSV file into a DataFrame with appropriate encoding and delimiter
    df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
    
    # Define the fields to keep
    fields_to_keep = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
    
    # Keep only the specified fields
    df_filtered = df[fields_to_keep]
    
    # Drop rows where any of the fields are empty
    df_filtered = df_filtered.dropna(subset=fields_to_keep)
    
    # Save the filtered DataFrame to a new CSV file
    df_filtered.to_csv(output_file, index=False, sep=';', encoding='latin1')
    
    return df_filtered

# Example usage
input_file = 'MICRODADOS_ENEM_2017.csv'  # Replace with your input file name
output_file = 'MICRODADOS_ENEM_2017_FILTRADOS.csv'  # Replace with your desired output file name
filtered_df = filter_csv_br(input_file, output_file)

print("Filtered DataFrame:")
print(filtered_df)
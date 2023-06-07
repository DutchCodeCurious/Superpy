import pandas as pd


def convert_csv(input_file, output_file, output_format):
    df = pd.read_csv(input_file)

    if output_format.lower() == 'json':
        # Convert DataFrame to JSON and save to output file
        df.to_json(output_file, orient='records')
        print(f"CSV file '{input_file}' converted to JSON: '{output_file}'")

    elif output_format.lower() == 'excel':
        # Convert DataFrame to Excel and save to output file
        df.to_excel(output_file, index=False)
        print(f"CSV file '{input_file}' converted to Excel: '{output_file}'")

    else:
        print("Invalid output format specified. Please choose 'json' or 'excel'")

#main.py
#This script takes the text files outputted from the BioSemi ActiveTwo program when making peaks from
#.BDF files 

#imports
import pandas as pd
import re


def toCSV(rowpath, colpath, vals, filename):

    # Make the row (this will be the 'Participant' ID)
    with open(rowpath, 'r', encoding='UTF-8') as file:
        rows = [line.strip() for line in file]
    print("ROWS: ", rows)

    if len(rows) != 1:
        raise ValueError("Expected exactly 1 row (participant), but got multiple rows.")

    # Make the column headers (192 other columns)
    with open(colpath, 'r', encoding='UTF-8') as file:
        cols = ["Participant"] + [line.strip() for line in file]
    print("COLUMNS: ", cols)

    # Read and fix the values (1 row with 192 values)
    def fix_ws(v):
        with open(v, 'r') as file:
            content = file.read()  # Read all content at once
            # Replace multiple spaces with a single comma
            fixed_content = re.sub(r'\s+', ',', content.strip())
        return fixed_content.split(',')

    slav = fix_ws(vals)  # Should result in 192 values; slav is just vals spelt backwards, I'm not original...
    print("VALUES: ", slav)

    # Validate the number of values (192 values + 1 participant = 193 columns)
    if len(slav) != len(cols) - 1:
        raise ValueError(f"Expected {len(cols) - 1} values, but got {len(slav)}.")

    # Create DataFrame: 1 row, 193 columns
    data = [[rows[0]] + slav]  # Combine participant ID with values
    df = pd.DataFrame(data, columns=cols)

    print("DATAFRAME: ")
    print(df)

    # Save to Excel
    df.to_excel(filename, index=False)

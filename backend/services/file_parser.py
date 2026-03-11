import pandas as pd

def parse_file(file):

    # check file type
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)

    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(file.file)

    else:
        raise Exception("Unsupported file format")

    # only send first rows to AI
    return df.head(10).to_string()
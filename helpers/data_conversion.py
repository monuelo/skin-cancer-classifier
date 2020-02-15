import pandas as pd

def create_csv(file, extension):
    """Create a CSV file from a xls
        Args:
            file: The file path that will be converted without the extension
            extension: The file extension
    """
    data_xls = pd.read_excel(f"{file}.{extension}", index_col=None)
    data_xls.to_csv(f"{file}.csv", encoding='utf-8')
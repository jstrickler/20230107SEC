import pandas as pd
import openpyxl as px


def main():
    """program entry point"""
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb['US Presidents']
    print_first_and_last_names(ws)


def print_first_and_last_names(ws):
    pres_range = ws['B2':'E20']  # cell range
    df = pd.DataFrame((c.value for c in row) for  row in pres_range)
    print(df.head())

if __name__ == '__main__':
    main()

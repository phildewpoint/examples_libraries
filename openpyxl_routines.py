from openpyxl import worksheet as ws
from openpyxl import workbook as wb
import openpyxl as op


def copy_worksheet_values(source_worksheet: ws.Worksheet, target_worksheet: ws.Worksheet):
    """
    Copies cell values from the source worksheet to the target worksheet


    Keyword arguments:
    source_worksheet -- the source (starting) worksheet to copy from
    target_worksheet -- the target worksheet to copy data to
    """
    rows = []
    for row in source_worksheet.iter_rows():
        row_data = []
        for cell in row:
            row_data.append(cell.value)
        rows.append(row_data)
    for source_rows in rows:
        target_worksheet.append(source_rows)

import openpyxl

# get workbook object; the data_only option captures the current value of any formulae
# Your file should be in the same directory as this code, OR you need to provide the FULL path to that file, not just it's name
demo_workbook = openpyxl.load_workbook('demo_workbook.xlsx', data_only= True)

# WB -> WS -> Cell
demo_worksheet = demo_workbook.get_sheet_by_name("clean_data")
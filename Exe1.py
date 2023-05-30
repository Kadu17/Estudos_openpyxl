from openpyxl import load_workbook
wb = load_workbook('C:/Users/50947025804/PycharmProjects/Openpyxl/teste.xlsx')
plan = wb.active
plan['P1'] = 'N'
wb.save('C:/Users/50947025804/PycharmProjects/Openpyxl/teste.xlsx')
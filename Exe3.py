from openpyxl import load_workbook
wb = load_workbook('C:/Users/50947025804/PycharmProjects/Openpyxl/teste.xlsx')
p = wb['P3']

for i in range(1, 20):
    p[f'A{i}'] = i

wb.save('C:/Users/50947025804/PycharmProjects/Openpyxl/teste.xlsx')
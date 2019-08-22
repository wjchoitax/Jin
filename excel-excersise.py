from openpyxl import load_workbook

# 엑셀을 읽어온다
xlsx = load_workbook('C:\\Python\\examples\\06\\2017.12.1.xlsx')
sheet = xlsx.active

# 세번째 열을 가져옴
col = sheet['C']

# 세번째 열의 각 행 값을 출력
for cell in col:
    print(cell.value)

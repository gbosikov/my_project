import json
import pandas as pd
import openpyxl

with open('body_types', 'r', encoding='utf-8') as bt:
    data = json.load(bt)


workbook = openpyxl.Workbook()
worksheet = workbook.active
headers = ['bodyTypeId', 'nameEnglish', 'nameGeorgian']
worksheet.append(headers)

for row in data:
    worksheet.append([row[header] for header in headers])



workbook.save('data.xlsx')
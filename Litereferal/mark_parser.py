import json
import pandas as pd
import openpyxl

with open('body_types', 'r', encoding='utf-8') as bt:
    data = json.load(bt)

idx = 0
for val in data:
    print(val['bodyTypeId'])
    df = pd.DataFrame([[val['bodyTypeId']], [val['nameEnglish']], [val['nameGeorgian']]],
                      index=[x for x in range(3)])
    df.to_excel('body_type.xlsx', sheet_name='body_type', index=False, header=False)
    print(df)

df5 = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])
print(df5)

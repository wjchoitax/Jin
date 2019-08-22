import pandas as pd

# df = pd.read_excel('Product list.xlsx')
df = pd.read_csv('C:\\python-study\\examples\\05\\csv_files\\2017.01.csv')
# print(df['수강금액'].sum())

new_df = df.loc[df['수강금액'] >= 800000]

new_df.to_excel('고액수강생.xlsx', index=False)

print('Save ok..')
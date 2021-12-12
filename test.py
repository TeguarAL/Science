import pandas as pd

pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

excel = pd.read_excel(r'Data RBE.xlsx')
excel.to_csv(r'Data RBE.csv', index=None, header=True)
df = pd.read_csv(r'Data RBE.csv')
df = df.drop(columns=['Unnamed: 17', 'Unnamed: 18'], axis=1)
df.to_csv(r'Data RBE.csv', index=None, header=True)
print(df)
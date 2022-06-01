import pandas as pd
import seaborn as sns

df = pd.read_excel('s2220106.xlsx')
df.to_csv('mod.cvs', index=False)

print(df.columns[0])
print(df[df.columns[0]] == 'H')

a = df[df.columns[0]] == 'H'

print(df.index[0])






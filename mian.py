import pandas as pd

df = pd.read_excel('novy_bez.xlsx')

df.to_csv('mod.cvs', index=True)

print(df.iloc[0, 0])
import pandas as pd


df = pd.read_excel('test.xlsx')
one = df['one'].tolist()
two = []
for i in range(len(one)):
    two.append(int('yes' in one[i]))
print(two)
df['two'] = two
print(df)
import pandas as pd
df = pd.read_csv("goodreadsbooks.csv")

print(df)

print(df.isnull().sum())

print(df.dtypes)

print(df.describe())

df.replace(to_replace='J.K. Rowling/Mary GrandPré', value = 'J.K. Rowling', inplace=True)

print(df)




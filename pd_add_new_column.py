import pandas as pd

df = pd.read_csv('ecommerce_sales_data.csv', nrows=10)
df["Tax"] = df["Revenue"] * .20
df.to_csv('data_with_tax1.csv', index=False)

print(df)





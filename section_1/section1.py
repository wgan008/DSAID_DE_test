import pandas as pd
from datetime import date

df = pd.read_csv("dataset.csv")
print("Raw count is: ",df.count())

df = df[(pd.notnull(df["name"])) | (df["name"]!='')]

df['first_name'], df['last_name'] = df['name'].str.split(' ', 1).str

df["aboce_100"] = df["price"] > 100

filename = date.today().strftime('%Y%m%d') + "_res.csv"
df.to_csv(filename)
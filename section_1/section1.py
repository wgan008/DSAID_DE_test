import pandas as pd
from datetime import date
import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('i',
                       type=str,
                       default='',
                       help='the path to src file')

my_parser.add_argument('o',
                       type=str,
                       default='',
                       help='the path to result file')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.i
output_path = args.o

df = pd.read_csv(input_path)
print("Raw count is: ",df.count())

# remove null or empty name
df = df[(pd.notnull(df["name"])) | (df["name"]!='')]

# split name into first and last names
df['first_name'], df['last_name'] = df['name'].str.split(' ', 1).str

# mark price > 100
df["above_100"] = df["price"] > 100

# create result file with date in name
filename = date.today().strftime('%Y%m%d') + "_res.csv"
df.to_csv(output_path + filename)
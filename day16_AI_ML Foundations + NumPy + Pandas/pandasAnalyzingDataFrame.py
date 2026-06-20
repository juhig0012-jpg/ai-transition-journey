#Get a quick overview by printing the first 10 rows of the DataFrame:
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

#Print the first 5 rows of the DataFrame:
df = pd.read_csv('data.csv')

print(df.head())

#Print the last 5 rows of the DataFrame:
print(df.tail())

#Print information about the data:
print(df.info()) 

#Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data.


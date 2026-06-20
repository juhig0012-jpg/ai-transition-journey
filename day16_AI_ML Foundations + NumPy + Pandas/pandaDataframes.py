#Create a DataFrame from two Series:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

#Return row 0:
print(myvar.loc[0])

#Return row 0 and 1
print(myvar.loc[[0, 1]])

#Add a list of names to give each row a name:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#Return "day2":

print(df.loc["day2"])

#Load a comma separated file (CSV file) into a DataFrame:
#If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

df = pd.read_csv('students.csv')

print(df) 

#Load the CSV into a DataFrame:
#Tip: use to_string() to print the entire DataFrame.
df = pd.read_csv('students.csv')

print(df.to_string()) 

#You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows) 
#In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

#Increase the maximum number of rows to display the entire DataFrame:

pd.options.display.max_rows = 9999

df = pd.read_csv('students.csv')

print(df)
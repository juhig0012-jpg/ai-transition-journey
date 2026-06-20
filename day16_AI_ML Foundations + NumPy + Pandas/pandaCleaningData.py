#Return a new Data Frame with no empty cells:
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

#Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

#If you want to change the original DataFrame, use the inplace = True argument:
#Remove all rows with NULL values:
df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

#Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

#Replace NULL values with the number 130:
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

#Replace NULL values in the "Calories" columns with the number 130:
df = pd.read_csv('data.csv')

df.fillna({"Calories": 130}, inplace=True)

#Calculate the MEAN, and replace any empty values with it:
#Mean = the average value (the sum of all values divided by number of values).
df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)

#Calculate the MEDIAN, and replace any empty values with it:
#Median = the value in the middle, after you have sorted all values ascending.

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

#Calculate the MODE, and replace any empty values with it:
#Mode = the value that appears most frequently.
df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

#Data of Wrong Format
#In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:
#Convert to date:
df = pd.read_csv('dateData.csv')

print(df.head())
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

#As you can see from the result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.

#Removing Rows
#Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace = True)

#Replacing Values
#One way to fix wrong values is to replace them with something else.

#In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
df.loc[7, 'Duration'] = 45

#If the value is higher than 120, set it to 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

#Delete rows where "Duration" is higher than 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

#Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

#Remove all duplicates:
df.drop_duplicates(inplace = True)

#Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.


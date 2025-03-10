import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
print("-------")

# Basic data manipulation
# Filtering rows where Age > 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)
print("-------")

# Grouping and aggregating
# TODO come up with better example
# grouped = df.groupby('Age').mean()
# print(grouped)
# print("-------")

# Adding a new column
df['Bonus'] = df['Salary'] * 0.10
print(df)
print("-------")

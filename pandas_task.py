""""🐼 Pandas Practice: DataFrames, Selection, Mapping, and More"""
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Sample data
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']
departments = ['Sales', 'Marketing', 'HR', 'Tech']

# Create a DataFrame
df = pd.DataFrame({
    'Name': np.random.choice(names, size=20),
    'Age': np.random.randint(22, 60, size=20),
    'Department': np.random.choice(departments, size=20),
    'Salary': np.random.randint(40000, 120000, size=20),
    'YearsExperience': np.random.randint(0, 20, size=20)
})
df.head()


"""Use .loc to select all rows where the Department is 'Tech'."""

tech_dept = df.loc[df['Department'] == 'Tech']
print(tech_dept)

""" Use .iloc to select the first 5 rows and the last two columns."""
first = df.iloc[:5,-2:]

"""Map a new column called 'DeptCode' where:"""
dept_map = {
    'Sales': 1,
    'Marketing': 2,
    'HR': 3,
    'Tech': 4
}
df['DeptCode'] = df['Department'].map(dept_map)

"""Use .apply to calculate a new column 'Seniority' where:"""
df['Seniority'] = df['YearsExperience'].apply(
    lambda x: 'Senior' if x > 10 else ('Mid-Level' if x >= 5 else 'Junior')
)
df.head()

"""Overwrite all salaries for employees with < 3 years of experience to 35000."""

condition = df['YearsExperience'] < 3

df.loc[condition,'Salary'] = 35000


"""Compare using .loc and .iloc to select the same row:"""

row_iloc = df.iloc[2]

index_label = df.index[2]

row_loc = df.loc[index_label]

"""Check if there are any duplicate names in the dataset."""

duplicates = df[df['Name'].duplicated(keep=False)]
print(duplicates)

"""Sort the DataFrame by Salary in descending order."""


df_sorted_salary = df.sort_values(by='Salary', ascending=False)
print(df_sorted_salary)

df_sorted_dept_age = df.sort_values(by=['Department', 'Age'])

"""Slice the DataFrame to return rows 5 through 12 and columns 'Name', 'Salary'"""

# using label-based : loc

label_based = df.loc[5:12,['Name','Salary']]

print(label_based)

print('*'*40)

# using position-based : iloc
salary_column_label_based = df.columns.get_loc('Salary')
name_column_label_based = df.columns.get_loc('Name')

position_based = df.iloc[5:13,[name_column_label_based,salary_column_label_based]]

print(position_based)


""" Find all rows where the name starts with 'A' or 'D'."""

names = df[df['Name'].str.startswith(('A', 'D'))]
print(names)

"""Drop all rows where Age is below 25."""

# Return a copy without modifying the original
df_filtered = df[df['Age'] >= 25]

# OR modify in place and modify the original :
df.drop(df[df['Age'] < 25].index, inplace=True)


"""Use groupby to calculate the average salary per Department."""
average_salary = df.groupby('Department')['Salary'].mean()
print(average_salary)

"""Use groupby to count how many employees are in each Department."""

employees_count = df.groupby('Department').size()
print(employees_count)


""" Use .apply to normalize the Salary column (min-max scaling between 0 and 1)."""

def normalize(x):
    return (x - x.min()) / (x.max() - x.min())

df['NormalizedSalary'] = df[['Salary']].apply(normalize)


"""Use boolean indexing to find all employees who:
- Are in 'HR' OR 'Tech', AND have > 5 years of experience."""

filtered_df = df[
    ((df['Department'] == 'HR') | (df['Department'] == 'Tech')) &
    (df['YearsExperience'] > 5)
]
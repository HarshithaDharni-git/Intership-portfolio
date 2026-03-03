# Task 1
# Data Overview
import pandas as pd
df=pd.read_excel("Data.xlsx")
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


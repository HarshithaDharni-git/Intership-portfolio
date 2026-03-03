import pandas as pd

# Load dataset
df=pd.read_excel("data.xlsx")

# Identify numerical columns automatically
numerical_columns=df.select_dtypes(include=['int64','float64']).columns
print("Numerial Columns:")
print(numerical_columns)
print("\nDescriptive Statistics:\n")

# Calculate mean, median, std for each numerical column
for column in numerical_columns:
    print(f"column: {column}")
    print("mean:",df[column].mean())
    print("median:",df[column].median())
    print("Standard Deviation:",df[column].std())
    print("-"*40)
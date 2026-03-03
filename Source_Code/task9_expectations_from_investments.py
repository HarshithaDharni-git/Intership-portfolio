import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Column name for expectations
column_name = "Expect"

# Clean text
df[column_name] = df[column_name].str.strip().str.title()

# Count frequency
expectation_counts = df[column_name].value_counts()

print("Expectations Frequency:")
print(expectation_counts)

# Identify most common expectation
most_common_expectation = expectation_counts.idxmax()
highest_count = expectation_counts.max()

print("\nMost Common Expectation from Investment:")
print(f"{most_common_expectation} ({highest_count} responses)")

# Create bar chart
expectation_counts.plot(kind='bar')

plt.title("Expectations from Investments")
plt.xlabel("Expectation")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.savefig("task9_expectations_distribution.png")

plt.show()

# Save results to Excel
expectation_counts.to_excel("task9_expectations_frequency.xlsx")
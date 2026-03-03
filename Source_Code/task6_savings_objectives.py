import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Exact column name from your dataset
column_name = "What are your savings objectives?"

# Clean text
df[column_name] = df[column_name].str.strip().str.title()

# Count frequency
objective_counts = df[column_name].value_counts()

print("Savings Objectives Frequency:")
print(objective_counts)

# Identify main objective
most_common_objective = objective_counts.idxmax()
highest_count = objective_counts.max()

print("\nMain Savings Objective:")
print(f"{most_common_objective} ({highest_count} responses)")

# Create bar chart
objective_counts.plot(kind='bar')

plt.title("Savings Objectives Distribution")
plt.xlabel("Savings Objective")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.savefig("task6_savings_objectives.png")

plt.show()

# Save results to Excel
objective_counts.to_excel("task6_savings_objectives_frequency.xlsx")
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Clean Investment_Avenues column
df["Investment_Avenues"] = df["Investment_Avenues"].str.strip().str.title()

# Frequency count
investment_counts = df["Investment_Avenues"].value_counts()

print("\nInvestment Avenue Frequency:")
print(investment_counts)

# Identify most preferred
most_preferred = investment_counts.idxmax()
highest_count = investment_counts.max()

print("\nMost Preferred Investment Avenue:")
print(f"{most_preferred} ({highest_count} responses)")

# Create Bar Chart
investment_counts.plot(kind='bar')

plt.title("Investment Avenue Distribution")
plt.xlabel("Investment Avenue")
plt.ylabel("Count")

plt.xticks(rotation=45)

# Save chart
plt.savefig("task4_investment_distribution.png")

plt.show()

# Save frequency to Excel
investment_counts.to_excel("task4_investment_frequency.xlsx")
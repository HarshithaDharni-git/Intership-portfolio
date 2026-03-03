import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Clean text (lowercase to match properly)
df["Duration"] = df["Duration"].str.strip().str.lower()

# Correct mapping based on your actual values
duration_mapping = {
    "less than 1 year": 0.5,
    "1-3 years": 2,
    "3-5 years": 4,
    "more than 5 years": 6
}

# Convert to numeric
df["Duration_Numeric"] = df["Duration"].map(duration_mapping)

# Calculate average duration
average_duration = df["Duration_Numeric"].mean()

print("Average Investment Duration:")
print(round(average_duration, 2), "Years")

# Optional: show distribution
df["Duration"].value_counts().plot(kind='bar')

plt.title("Investment Duration Distribution")
plt.xlabel("Duration")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.savefig("task8_investment_duration_distribution.png")

plt.show()
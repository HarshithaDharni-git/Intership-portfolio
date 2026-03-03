import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Select reason columns
reason_columns = [
    "Reason_Equity",
    "Reason_Mutual",
    "Reason_Bonds",
    "Reason_FD"
]

# Combine all reasons into one column
all_reasons = pd.concat([df[col] for col in reason_columns])

# Clean text
all_reasons = all_reasons.dropna().str.strip().str.title()

# Count frequency
reason_counts = all_reasons.value_counts()

print("Reason Frequency:")
print(reason_counts)

# Most common reason
most_common_reason = reason_counts.idxmax()
highest_count = reason_counts.max()

print("\nMost Common Reason for Investment:")
print(f"{most_common_reason} ({highest_count} responses)")

# Create bar chart
reason_counts.plot(kind='bar')

plt.title("Reasons for Investment")
plt.xlabel("Reason")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.savefig("task5_reasons_distribution.png")

plt.show()

# Save to Excel
reason_counts.to_excel("task5_reason_frequency.xlsx")
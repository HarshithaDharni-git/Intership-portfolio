import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Column name for information source
column_name = "Source"

# Clean text
df[column_name] = df[column_name].str.strip().str.title()

# Count frequency
source_counts = df[column_name].value_counts()

print("Information Sources Frequency:")
print(source_counts)

# Identify most common source
most_common_source = source_counts.idxmax()
highest_count = source_counts.max()

print("\nMost Common Information Source:")
print(f"{most_common_source} ({highest_count} responses)")

# Create bar chart
source_counts.plot(kind='bar')

plt.title("Common Investment Information Sources")
plt.xlabel("Source")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.savefig("task7_information_sources.png")

plt.show()

# Save results to Excel
source_counts.to_excel("task7_information_sources_frequency.xlsx")

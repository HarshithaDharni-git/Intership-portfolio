import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Check column names
print(df.columns)

# Clean gender column
df["gender"] = df["gender"].str.strip().str.title()

# Count gender values
gender_counts = df["gender"].value_counts()

print("\nGender Distribution")
print(gender_counts)

# Create Bar Chart
gender_counts.plot(kind='bar')

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

# Save the chart
plt.savefig("gender_bar_chart.png")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data.xlsx")

# Clean Duration column
df["Duration"] = df["Duration"].str.strip().str.lower()

# Convert Duration to numeric
duration_mapping = {
    "less than 1 year": 0.5,
    "1-3 years": 2,
    "3-5 years": 4,
    "more than 5 years": 6
}

df["Duration_Numeric"] = df["Duration"].map(duration_mapping)

# Select relevant numerical columns
correlation_columns = ["age", "Duration_Numeric"]

# Create correlation matrix
correlation_matrix = df[correlation_columns].corr()

print("Correlation Matrix:")
print(correlation_matrix)

# Visualize correlation matrix
plt.imshow(correlation_matrix, cmap='coolwarm')
plt.colorbar()

plt.xticks(range(len(correlation_columns)), correlation_columns)
plt.yticks(range(len(correlation_columns)), correlation_columns)

plt.title("Correlation Matrix")

plt.savefig("task10_correlation_matrix.png")
plt.show()

# Scatter plot (Age vs Duration)
plt.scatter(df["age"], df["Duration_Numeric"])

plt.title("Age vs Investment Duration")
plt.xlabel("Age")
plt.ylabel("Investment Duration (Years)")

plt.savefig("task10_age_vs_duration.png")
plt.show()
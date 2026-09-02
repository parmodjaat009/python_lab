import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display rows and columns
print("Shape of dataset:", df.shape)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display summary
print("\nSummary:")
print(df.describe())

# Filter data
filtered_data = df[df["Marks"] > 80]

# Display filtered data
print("\nFiltered Data:")
print(filtered_data)

# Save filtered data
filtered_data.to_csv("filtered_data.csv", index=False)

print("\nData exported successfully!")
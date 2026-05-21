import pandas as pd
import random

# Number of rows to generate
num_rows = 1000

# Sample data generation
data = {
    'ID': range(1, num_rows + 1),
    'Name': [f"User_{i}" for i in range(1, num_rows + 1)],
    'Age': [random.randint(18, 70) for _ in range(num_rows)],
    'Email': [f"user{i}@example.com" for i in range(1, num_rows + 1)],
    'Salary': [random.randint(30000, 120000) for _ in range(num_rows)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV in your current VS Code folder
df.to_csv('sample_data.csv', index=False)

print(f"Successfully generated {num_rows} records in 'sample_data.csv'")

import pandas as pd
import numpy as np

# 1. Read the original CSV file
input_file = 'sample_data.csv'  # Change to your actual file name
df = pd.read_csv(input_file)

# 2. Split the DataFrame into 3 equal chunks
chunks = np.array_split(df, 3)

# 3. Save each chunk into a new file
for i, chunk in enumerate(chunks):
    output_file = f'chunk_{i+1}.csv'
    chunk.to_csv(output_file, index=False)
    print(f"Saved {len(chunk)} rows to {output_file}")

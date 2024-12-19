import pandas as pd

# Paths to the datasets
false_path = "data/Fake.csv"
true_path = "data/True.csv"
output_path = "data/dataset.csv"

# Load datasets
print("Loading datasets...")
false_data = pd.read_csv(false_path)
true_data = pd.read_csv(true_path)

# Add labels: 1 = Fake, 0 = Real
print("Adding labels...")
false_data['label'] = 1
true_data['label'] = 0

# Combine datasets
print("Combining datasets...")
combined_data = pd.concat([false_data, true_data], ignore_index=True)

# Shuffle the data
print("Shuffling the combined dataset...")
combined_data = combined_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the combined dataset
print(f"Saving the combined dataset to {output_path}...")
combined_data.to_csv(output_path, index=False)

print("Dataset preparation complete.")

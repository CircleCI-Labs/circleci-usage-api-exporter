import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# List all CSV files in the 'reports' directory
csv_files = glob.glob('/tmp/reports/*.{}'.format('csv'))

print("Finding all csv files, and merging...")

# Merge the CSV files together
merged_file_path = '/tmp/reports/merged.csv'
with open(merged_file_path, 'w') as merged_file:
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            # Skip the header if not the first file
            if csv_file != csv_files[0]:
                next(f)
            for line in f:
                merged_file.write(line)

# Read the merged CSV data into a pandas dataframe
df = pd.read_csv(merged_file_path)

# Group the data by 'PROJECT_NAME' and 'VCS_URL', and calculate the sum of 'TOTAL_CREDITS' for each group
grouped_df = df.groupby(['PROJECT_NAME', 'VCS_URL'])['TOTAL_CREDITS'].sum()

# Sort the grouped dataframe by 'TOTAL_CREDITS' in descending order
sorted_df = grouped_df.sort_values(ascending=False)


# Save the sorted dataframe into a CSV file
sorted_file_path = 'sorted_credits.csv'
sorted_df.to_csv(sorted_file_path, header=True)

# Print message after saving the sorted DataFrame
print(f"Sorted data saved to {sorted_file_path}")

# Filter out rows with 0 total credits
print("To reduce graph noise, removing all projects that have 0 credits spent")
grouped_df = grouped_df[grouped_df != 0]

# Create a bar plot to show total credits per project
plt.figure(figsize=(15, 10))
grouped_df.plot(kind='bar')
plt.ylabel('Total Credits')
plt.xlabel('Project')
plt.title('Total Credits per Project')

# Save the plot as an artifact
plt.savefig('/tmp/reports/total_credits_per_project.png', bbox_inches='tight')

# Print the total credits per project
print(grouped_df)

# Print message after saving the plot
print("Plot saved as 'total_credits_per_project.png' in the reports directory")
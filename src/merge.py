# Import modules
import os
import glob

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

print("csv files merged")
import pandas as pd

import os

file_path = 'Alldata.csv'  # Replace with the correct file name
if os.path.isfile(file_path):
    print("File exists")
else:
    print("File not found")


# Load the Excel dataset into a Pandas DataFrame
df = pd.read_csv('F:\Anime Recom\Alldata.csv')  # Replace 'your_dataset_file.xlsx' with the actual file path

# Display the first few rows of the dataset
print(df.head())

# Get the dimensions of the dataset (rows, columns)
print(df.shape)

# Get a summary of the dataset, including data types and missing values
print(df.info())

# Get basic statistics of the numerical columns
print(df.describe())



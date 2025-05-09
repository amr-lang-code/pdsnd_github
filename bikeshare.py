import pandas as pd

# Load the dataset
file_path = "/mnt/data/student_habits_performance.csv"
df = pd.read_csv(file_path)

# Display basic info and first few rows
df_info = df.info()
df_head = df.head()
df_description = df.describe(include='all')

df_info, df_head, df_description
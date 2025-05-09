import pandas as pd

# Load the dataset
file_path = "/mnt/data/student_habits_performance.csv"
df = pd.read_csv(file_path)

# Display basic info and first few rows
df_info = df.info()
df_head = df.head()
df_description = df.describe(include='all')

df_info, df_head, df_description

import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Plot distribution and boxplot for exam_score
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Distribution plot
sns.histplot(df['exam_score'], kde=True, bins=30, ax=axes[0])
axes[0].set_title('Distribution of Exam Scores')
axes[0].set_xlabel('Exam Score')
axes[0].set_ylabel('Count')

# Boxplot
sns.boxplot(x=df['exam_score'], ax=axes[1])
axes[1].set_title('Boxplot of Exam Scores')
axes[1].set_xlabel('Exam Score')

plt.tight_layout()
plt.show()

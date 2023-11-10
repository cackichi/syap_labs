import pandas as pd
import matplotlib.pyplot as plt

file_path = 'E:\CYAPlabs\lab5/test.csv'
df = pd.read_csv(file_path)
df_subset = df.head(1000)
missing_val = df_subset.isnull().sum()
print(missing_val)

plt.boxplot(df_subset['Square'], vert=False)
plt.xscale('log')
plt.show()

plt.hist(df_subset['Square'], bins=20)
plt.xlabel('Square')
plt.ylabel('Frequency')
plt.show()

df_subset_copy = df_subset.copy()
numeric_columns = df_subset_copy.select_dtypes(include='number').columns
for column in numeric_columns:
    df_subset_copy[column].fillna(df_subset_copy[column].median(), inplace=True)
    df_subset_copy[column] = df_subset_copy[column].replace(0, df_subset_copy[column].median())

room_counts = df_subset_copy['Rooms'].value_counts()
print(room_counts)

pivot_table = pd.pivot_table(df_subset_copy, values='Id', index='DistrictId', columns='Rooms', aggfunc='count', fill_value=0)
print("Pivot table: \n", pivot_table)

save_file_path = 'E:\CYAPlabs\lab5\surname.csv'
df_subset_copy.to_csv(save_file_path, index=False)
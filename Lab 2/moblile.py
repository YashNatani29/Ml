import matplotlib.pyplot as plt
import pandas as pd


# Reading CSV files
data1 = pd.read_csv("android_devices.csv")
data2 = pd.read_csv("user_device.csv")
data3 = pd.read_csv("user_usage.csv")

# using merge function to merge csv file
output1 = pd.merge(data2, data1, on='Device')
output2 = pd.merge(output1, data3, on='use_id')

# Creating CSV of merged file
output2.to_csv('merged.csv', index=False)
print(output2)

# applying basics stats function
print(output2.describe())

print("\nNumber of Users")
print(output2['Retail Branding'].value_counts())

df = pd.read_csv('merged.csv', index_col=0)

# Grouping the data by Retail Branding
df_rank = df.groupby('Retail Branding')
print(df_rank.groups)

# Calculating sum of data
mins = df_rank['outgoing_mins_per_month'].sum()
sms = df_rank['outgoing_sms_per_month'].sum()
mb = df_rank['monthly_mb'].sum()

# Contacting data, changing columns name and saving the data to csv
python_df = pd.concat([mins, sms, mb], axis='columns', sort=False)
python_df.rename(
    columns={'outgoing_mins_per_month': 'Total Mins', 'outgoing_sms_per_month': 'Total sms', 'monthly_mb': 'Total mbs'},
    inplace=True)
print(python_df)
python_df.to_csv('summery.csv', index=False)

arr = mins.to_numpy()
arr1 = sms.to_numpy()
arr2 = mb.to_numpy()
rd = df_rank.groups.keys()

#  creating the bar plot
plt.subplot(1, 3, 1)
plt.bar(rd, arr, color='yellow', width=0.4)
y_pos = range(len(rd))
plt.xticks(y_pos, rd, rotation=90)
plt.xlabel('Mobile Company')
plt.ylabel('Total Outgoing call in mins: ')

plt.subplot(1, 3, 2)
plt.bar(rd, arr1, color='blue', width=0.4)
y_pos = range(len(rd))
plt.xticks(y_pos, rd, rotation=90)
plt.xlabel('Mobile Company')
plt.ylabel('Total outgoing sms ')
plt.title('Usage across different mobile company: ')

plt.subplot(1, 3, 3)
plt.bar(rd, arr2, color='red', width=0.4)
y_pos = range(len(rd))
plt.xticks(y_pos, rd, rotation=90)
plt.xlabel('Mobile Company')
plt.ylabel('Total Monthly_mb ')

plt.show()

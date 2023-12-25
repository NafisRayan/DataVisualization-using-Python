import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Load CSV data into a DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Income': [5000] * 12,
    'Rent': [1200] * 12,
    'Utilities': [200] * 12,
    'Groceries': [300] * 12,
    'Entertainment': [200] * 12,
    'Transportation': [100] * 12,
    'Savings': [1000] * 12
}

df = pd.DataFrame(data)

# Plotting pie chart for a specific month (e.g., January)
month_data = df.loc[df['Month'] == 'January', ['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Transportation', 'Savings']]
labels = month_data.columns
sizes = month_data.iloc[0].values

plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Monthly Expenses for January')
plt.show()

# Plotting bar chart for all months
plt.figure(figsize=(10, 6))
df.set_index('Month').plot(kind='bar', stacked=True)
plt.title('Monthly Expenses Breakdown')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.show()

# Creating a Venn diagram for Savings and Entertainment for January and February
january_set = set(df.loc[df['Month'] == 'January', 'Entertainment'])
february_set = set(df.loc[df['Month'] == 'February', 'Savings'])

venn2([january_set, february_set], set_labels=('Entertainment (January)', 'Savings (February)'))
plt.title('Venn Diagram: Entertainment (January) vs. Savings (February)')
plt.show()

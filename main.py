import pandas as pd

#reading the csv file
data = pd.read_csv('transactions.csv')

#grouping the data by category and summing the amounts
expenses = data[data['Transaction Type'] == 'Expense']
transaction_Category = expenses.groupby(['Category'])
category_sum = transaction_Category['Amount'].sum() * -1

#grouping the data by month and summing the amounts
transaction_month= data.groupby(['Month'])
month_sum = transaction_month['Amount'].sum()


#Printing the results
print("-- Transaction Category Summary --")
print(category_sum)
print("-- Transaction Month Summary --")
print(month_sum)
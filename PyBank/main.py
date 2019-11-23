#claudia ibarra
#python-challenge hw

#python-challenge is to create a python script that analyzes the records to calculate:
#number of months including the dataset, net total amount of "profit/losses"
#average of changes/greatest increase/greatest decrease in the "profit/losses"

#import modules
import os
import csv

budget_csv = os.path.join("../PyBank","budget_data.csv")

output_file = os.path.join("Bank Report")
#in the bank report, looking for:
#total months
#total amount
#average change
#greatest increase in profits month / amount
#greatest decrease in profits month / amount

#tee-ing up with variables
total_months = 0
total_profit = 0
profit = []
previous_profit = 0
month_of_change = []
profit_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
profit_change_list = []
profit_average = 0

#open budget csv file 
with open(budget_csv, 'r') as Bank_Report:
    csvreader = csv.DictReader(Bank_Report)
    for row in csvreader:
       #calculating total months
       total_months = total_months + 1
       #calculating total profit
       total_profit = total_profit + int(row["Profit/Losses"])
       #calculating profit change
       profit_change = float(row["Profit/Losses"]) - previous_profit
       #calculating previous profit
       previous_profit = float(row["Profit/Losses"])

print (total_months)
print (total_profit)
print (profit_change)
print (previous_profit)
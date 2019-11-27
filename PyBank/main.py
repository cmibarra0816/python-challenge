#claudia ibarra
#python-challenge hw

#python-challenge is to create a python script that analyzes the records to calculate:
#number of months including the dataset; net total amount of "profit/losses" overall;
#average of changes the "profit/losses" overall; greatest increase / decrease overall

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
       #calculating profit change list
        profit_change_list = profit_change_list + [profit_change]
       #calculating change of months
        month_of_change = [month_of_change] + [row["Date"]]
        if profit_change > greatest_increase[1]:
            greatest_increase[1]= profit_change
            greatest_increase[0] = row['Date']
        if profit_change < greatest_decrease[1]:
            greatest_decrease[1]= profit_change
            greatest_decrease[0] = row['Date']
    #calculating profit average
    profit_average = round(sum(profit_change_list[1:])/len(profit_change_list[1:]), 2)

#write changes to csv
with open(budget_csv, 'w') as Bank_Report:
    Bank_Report.write("Financial Analysis\n")
    Bank_Report.write("---------------------\n")
    Bank_Report.write("Total Months: %d\n" % total_months)
    Bank_Report.write("Total Profit: $%d\n" % total_profit)
    Bank_Report.write("Average Profit Change $%d\n" % profit_average)
    Bank_Report.write("Greatest Increase in Profit: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    Bank_Report.write("Greatest Decrease in Profit: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
#claudia ibarra
#python-challenge hw

#import modules
import os
import csv

budget_csv = os.path.join("../PyBank","budget_data.csv")

output_file = os.path.join("Bank Report")
#tee-ing up with variables
total_months = 0

#open budget csv file 
with open(budget_csv, 'r') as Bank_Report:
    csvreader = csv.DictReader(Bank_Report)
    for row in csvreader:
       total_months = total_months + 1
print (total_months)
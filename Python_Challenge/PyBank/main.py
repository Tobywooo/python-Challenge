# importing dependencies
import os
import csv
import pandas as pd
from pathlib import Path

#reads in the CSVs for PyBank
file = Path('PyBank', 'Resources', 'budget_data.csv')
file_Print= Path('PyBank', 'Analysis', "Analysis_Export.txt")

#declares variables and empty lists 
Total_Months = 0
Total = 0
Average_Change = 0

totalMonths = []
totalProfit = []
averageMonthlyChange = []

#Opening and reading the csv file
with open(file, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #reading the header row
    header = next(csvreader)

    #loops through the rows in the csv
    for row in csvreader:
        totalMonths.append(row[0])
        totalProfit.append(int(row[1]))

    #calculates monthly changes in profit/loss  and stores in averageMonthlyChange
    for i in range(len(totalProfit)-1):

        averageMonthlyChange.append(totalProfit[i+1] - totalProfit[i])

#Finds the max and min for profits per month
monthlyProfitMax = max(averageMonthlyChange)
monthlyProfitMin = min(averageMonthlyChange)

#finds the dates for the profits
monthlyProfitMaxDate = averageMonthlyChange.index(monthlyProfitMax) + 1
monthlyProfitMinDate = averageMonthlyChange.index(monthlyProfitMin) + 1

#calculates the final output
Total_Months=len(totalMonths)
Total = sum(totalProfit)
Average_Change = sum(averageMonthlyChange)/len(averageMonthlyChange)
Greatest_Increase_In_Profit_Date = totalMonths[monthlyProfitMaxDate]
Greatest_Decrease_In_Profit_Date = totalMonths[monthlyProfitMinDate]

#prints final analysis to console
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${round(Average_Change,2)}")
print(f"Greatest Increase in Profits: {Greatest_Increase_In_Profit_Date} (${(str(monthlyProfitMax))})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_In_Profit_Date} (${(str(monthlyProfitMin))})")

#writes the analysis to txt
with open(file_Print,'w') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------------------------------------")
    file.write("\n")
    file.write(f"Total Months: {Total_Months}")
    file.write("\n")
    file.write(f"Average Change: ${round(Average_Change,2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Greatest_Increase_In_Profit_Date} (${(str(monthlyProfitMax))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Greatest_Decrease_In_Profit_Date} (${(str(monthlyProfitMin))})")
    file.write("\n")
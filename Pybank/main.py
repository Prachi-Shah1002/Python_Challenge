import os
import csv

#creating an object out of the CSV file
budget_data = os.path.join("Resources/budget_data.csv")

total_month = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    #Reading the header row
    csv_header = next(csvreader)

    #reading the first row
    first_row = next(csvreader)
    total_month += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    #going through each row of data after header & first row
    for row in csvreader:
        dates.append(row[0])

        #calculate the change, then add it to list of changes
        change = int(row[1])- value
        profits.append(change)
        value = int(row[1])

        #Total number of months
        total_month +=1

        #Total net amount of Profit/Loss 
        total_pl = total_pl + int(row[1])

        
    #Greatest increase in Profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease in Profit
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in Profit/Loss 
    avg_change = sum(profits)/len(profits)

#Displaying information

print("Financial Analysis")
print("-------------------------")
print(f"Total Months : {str(total_month)}")
print(f"Total : ${str (total_pl)}")
print(f"Average Change:${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Exporting to .txt file
output = open("Analysis/output.txt","w")

line1 = "Financial Analysis"
line2 = "--------------------"
line3 =str(f"Total Months : {str(total_month)}")
line4 = str(f"Total : ${str (total_pl)}")
line5 = str(f"Average Change:${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

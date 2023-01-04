import os
import csv

input_path = os.path.join('..', 'Resources','budget_data.csv')

# Opening the source file
with open(input_path) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    
    # Skipping the header
    csvheader = next(csvreader)
    
    # Initializing the variables
    number_of_months = 0
    net_PL = 0
    sum_changes_PL = 0
    greatest_decrease=0
    greatest_increase =0

    # Creating a list that can be iterated to compare previous and current month
    current_month=[]

    # iterating through the csvreader object
    for row in csvreader:
        number_of_months +=1
        net_PL+=float(row[1])
        current_month.append(row)

# iterating through the list to calculate changes in profit/losses
for i in range(1, len(current_month)):
    change_PL = float(current_month[i][1])-float(current_month[i-1][1])
    sum_changes_PL += change_PL
    if change_PL > greatest_increase:
        greatest_increase = change_PL
        greatest_increase_month = current_month[i][0]
    if change_PL < greatest_decrease:
        greatest_decrease = change_PL
        greatest_decrease_month = current_month[i][0]

average_changes = sum_changes_PL/(number_of_months-1)

#   Printing results to the terminal
print("Financial Analysis \n -------------------------")

print(f" Total months:  {number_of_months} \n Total PL: {net_PL} \n Average Change: {average_changes} \n Greatest Increase in Profits: {greatest_increase_month} {greatest_increase} \nGreatest Decrease in Profits {greatest_decrease_month} {greatest_decrease}")

#   Creating an output variable
results = [number_of_months, net_PL, average_changes,greatest_increase_month, greatest_increase,greatest_decrease_month, greatest_decrease]

output_path = os.path.join("budget_analysis.csv")

#   Writing results to the output file
with open(output_path,"w") as csvwrite:
    csvwriter = csv.writer(csvwrite, delimiter=',')
    header = ["Total Months", "Total PL", "Average Change", "Month with Greatest Increase", "Greatest Increase", "Month with Greatest Decrease", "Greatest Decrease"]
    csvwriter.writerow(header)
    csvwriter.writerow(results)
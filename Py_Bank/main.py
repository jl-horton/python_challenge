import os 
import csv 
# Import the csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')
# Set initial variables
month_count = 0 
total_profloss = 0
max_inc = 0
max_dec = 0
max_inc_date = 0
max_dec_date = 0
total_change = 0
prev_profloss = 0
init_profloss = 0
final_profloss = 0
row_count = 0
# Open and read the csv file to find the requirements 
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read after the header row
    header = next(csvreader)
    # Read rows         
    for index, row in enumerate(csvreader):
        # Find the total number of months
        month_count += 1
        # Find the total profit/loss
        total_profloss += int(row[1])
        # Set conditionals to determine the first and last values in profit and loss
        if index == 0:
            init_profloss = float(row[1])
        elif index == row_count-1:
            final_profloss = float(row[1])    
        # Reset the last amount in profit and loss 
        final_profloss = float(row[1])  
        # Determine the change values in profit and loss from one to the next and so on
        change = float(row[1]) - prev_profloss
        # Determine the total change value from the sum of the values found
        total_change += change
        # Find the greatest increase in profits and loss from the changes
        if change >= max_inc:
            max_inc = int(change)  
            # Identify the date of the greatest increase in the corresponding date column
            max_inc_date = row[0]
        # Find the greatest decrease in profits and loss from the changes
        elif change <= max_dec:
            max_dec = int(change) 
            # Identify the date of the greatest decrease in the corresponding date column
            max_dec_date = row[0]
        # Save the updated previous profit and loss value
        prev_profloss = float(row[1])
    # Find the average change in profit and loss
    ave_change = ((final_profloss - init_profloss) / (month_count - 1))
    ave_change_rounded = round(ave_change,2)
    
# Define financial analysis data
file_data = f'''
Financial Analysis
---------------------------------------------------
Total Months: {str(month_count)}
Total: ${str(total_profloss)}
Average Change: ${str(ave_change_rounded)}
Greatest Increase in Profits: {str(max_inc_date)} (${str(max_inc)})
Greatest Decrease in Profits: {str(max_dec_date)} (${str(max_dec)})
'''
# Print data to the terminal
print(file_data)
# Specify financial analysis data output file and location
data_output = os.path.join("Analysis","PyBank_Financial_Analysis.txt")
# Write data as a text file
with open(data_output, "w") as txtfile:
    txtfile.write(file_data)
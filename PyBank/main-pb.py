import os
import csv

#Setting the path for csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Opening the csv file
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile,delimiter = ',')
	next(csvreader)

	total_row = 0
	net_total_amount = 0
	change = 0
	previous_row = 0
	max_increase = 0
	max_increase_month = ""
	max_decrease = 0
	max_decrease_month = ""
	
	for row in csvreader:
		# Calculate net total amount of Profit/Losses over the entire period
		net_total_amount = net_total_amount + int(row[1])
	
		#Calculate profit/losses change and skipping first row as previous months data not known
		difference = 0
		if total_row > 0:
			difference = int(row[1]) - previous_row
			change = change + difference
	
		previous_row = int(row[1])

		# Calculate greatest increase in profits
		if max_increase < difference:
			max_increase = difference
			max_increase_month = row[0]

		if max_decrease > difference:
			max_decrease = difference
			max_decrease_month = row[0]
	
		# Calculate total number of months included in the dataset
		total_row = total_row + 1
	
	# Number of changes is always one less than total number of rows
	average_change = change / (total_row - 1)

	#Create a txt file and print the result in the file	
	with open("Pybank.txt","w") as file:
		result = """
(Financial Analysis)
-------------------------------
Total Months: {}
Total Amount of Profit/Losses: {}
Average Change: {}
Greatest Increase in Profits: {} (${})
Greatest Decrease in Profits: {} (${})""".format(
	total_row, net_total_amount, round(average_change, 2), max_increase_month,
	 max_increase, max_decrease_month, max_decrease)

		# Writing the financial analysis in a .txt file
		file.write(result)
		print(result)

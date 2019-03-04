import os
import csv

#Setting the path for csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#Opening the csv file
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile,delimiter = ',')
	next(csvreader)
	total_votes = 0
	candidate = {}

	for row in csvreader:
		# Calculate total number of votes
		total_votes = total_votes + 1
		# List of candidates who received votes
		name = row[2]
	
		if name in candidate:
			candidate[name] = candidate[name] + 1
		else:
			candidate[name] = 1

	#Create a txt file and print the result in the file	
	with open("Pypoll.txt","w") as file:
		result = """
Election Results
-------------------------------
Total Votes: {}
-------------------------------
""".format(total_votes)
		print(result)
		file.write(result)
		max_votes = 0
		Winner = ""
		for name,votes in candidate.items():
			percent_votes = votes*100/total_votes
			if votes > max_votes:
				max_votes = votes
				Winner = name
			result = "{} : {}% ({})\n".format(name, round(percent_votes, 2),votes)
			print(result, end = '')
			file.write(result)

		result = """-------------------------------
Winner: {}
_______________________________""".format(Winner)

		file.write(result)

		print(result)
	
#The date we need to retrieve.
import csv
import os 
#Assign a variable for the file to load and the path 
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file.
with open(file_to_load) as election_data:
     #To do:read and analyze the data here.
    file_reader = csv.reader(election_data)

#print each row in the csv file
    headers = next(file_reader)
    print(headers)

#1. The total number of otes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner fo the election based on popular vote
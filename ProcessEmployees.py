"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file

infile = open("employee_data.csv", "r")
employeedata = csv.reader(infile, delimiter=",")
next(employeedata)

# create an empty dictionary

employeedict = {}


# use a loop to iterate through the csv file

print()
for item in employeedata:
    # check if the employee fits the search criteria
    if item[3] == "Marketing" and item[4] == "CSR":
        FullName = item[1] + " " + item[2]
        CurrentSalary = float(item[5])

        print(f"Manager Name: {FullName} Current Salary: ${(CurrentSalary):,.2f}")

        employeedict[f"{FullName}"] = (
            CurrentSalary * 1.10
        )  # assigns new salary to the Full Name key

print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout


for key, value in employeedict.items():
    print(f"Manager Name: {key} New Salary: ${value:,.2f}")

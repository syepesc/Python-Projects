"""
    Unix / Linux Operating Systems
    Assignment 03

    Author: Santiago Yepes
    Student number: 301082274
    Date:   Mar 29, 2020.

    Filename: copyfile.py
"""

"""
1) Write a script named copyfile.py. This script should prompt the user
for the names of two text files. The contents of the first file should be
input and written to the second file.
"""
print('1)')
pathFile1 = input('Enter the path for the first file name, include the extension on the file: ')
pathFile2 = input('Enter the path for the second file name, include the extension on the file: ')
content = input('Write the content for file 1: ')

file1 = open(pathFile1, 'a')
file1.write(f"{content}\n")
file1.close()

file1 = open(pathFile1, 'r')
file1Content = file1.readlines()

file2 = open(pathFile2, 'w')
for line in file1Content:
    file2.write(line)

file1.close()
file2.close()


"""
2) The Payroll Department keeps a list of employee information for each pay
period in a text file called data.txt. The format of each line of the file is the following:
<last name> <hourly wage> <hours worked>
Create 10 lines of data.

Write a program that inputs a filename from the user and prints to the
terminal a report of the wages paid to the employees for the given
period. The report should be in tabular format with the appropriate
header. Each line should contain an employee’s name, the hours worked,
and the wages paid for that period.
"""
print()
print('2)')

dataFile = open(input('Enter the data file name, include the extension on the file: '), 'r')
dataFileLines = dataFile.readlines()

print(': LAST NAME    : HOUR WAGE     : HOURS WORKED  : TOTAL PAID    :')
print('----------------------------------------------------------------')
for line in dataFileLines:
    lastName, hourWage, hoursWorked = line.strip().split(', ')
    totalPaid = int(hourWage) * int(hoursWorked)
    print(
        f' {lastName}{" " * (15 - len(lastName))} {hourWage}{" " * (15 - len(hourWage))} {hoursWorked}{" " * (15 - len(hoursWorked))} {str(totalPaid)}{" " * (15 - len(str(totalPaid)))}')
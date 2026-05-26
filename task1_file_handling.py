import os
import shutil
import csv
from datetime import date

# Task 1 - File Handling and Automation
# Name: Goudampally Sai Snehitha
# ID: BS/REG/120205

# todays date
today = str(date.today())

# making a text file for student results
f = open("results.txt", "w")
f.write("Student Result Report\n")
f.write("=====================\n")
f.write("Date: " + today + "\n")
f.write("Internship: Alfido Tech Training\n")
f.write("Subject: Python Programming\n")
f.write("Result: Pass\n")
f.write("Grade: A\n")
f.close()
print("results file created")

# reading the file
f = open("results.txt", "r")
lines = f.readlines()
print("\nfile data:")
for line in lines:
    print(line.strip())
f.close()

# making csv with student marks
f = open("marks.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow(["RollNo", "Name", "Python", "DSA", "DBMS", "Total", "Grade"])
writer.writerow(["001", "Snehitha", 92, 88, 85, 265, "A"])
writer.writerow(["002", "Charana", 78, 82, 80, 240, "B"])
writer.writerow(["003", "Ram", 95, 90, 92, 277, "A+"])
writer.writerow(["004", "Anumitha", 60, 65, 70, 195, "C"])
f.close()
print("\nmarks file created")

# printing all rows from csv
print("\nall student marks:")
f = open("marks.csv", "r")
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()

# filtering only grade A students
print("\ntop students:")
f = open("marks.csv", "r")
reader = csv.reader(f)
next(reader) # skipping first row (header)
for row in reader:
    if row[6] == "A" or row[6] == "A+":
        print(row[1], "got", row[5], "marks and grade", row[6])
f.close()

# finding who got highest marks
print("\nfinding topper...")
f = open("marks.csv", "r")
reader = csv.reader(f)
next(reader) # skip header
topper = ""
highest = 0
for row in reader:
    if int(row[5]) > highest:
        highest = int(row[5])
        topper = row[1]
f.close()
print(topper, "is topper with", highest, "marks")

# adding one more student to existing csv
f = open("marks.csv", "a", newline="")
writer = csv.writer(f)
writer.writerow(["005", "Kavya", 88, 91, 87, 266, "A"])
f.close()
print("\nnew student kavya added")

# creating folder and moving files
try:
    # create reports folder if not there
    if not os.path.exists("reports"):
        os.makedirs("reports")
        print("\nreports folder created")

    # renaming file with date
    os.rename("results.txt", "results_" + today + ".txt")
    print("file renamed")

    # moving file to reports folder
    shutil.move("results_" + today + ".txt", "reports/results_" + today + ".txt")
    print("file moved to reports")

    # copying csv to reports
    shutil.copy("marks.csv", "reports/marks_backup.csv")
    print("csv backup done")

    # removing original csv
    os.remove("marks.csv")
    print("original file deleted")

except FileNotFoundError:
    print("file not found")

except PermissionError:
    print("no permission to access file")

except Exception as e:
    print("error occured:", e)

# checking what is inside reports folder
print("\nreports folder has:")
for file in os.listdir("reports"):
    print("-", file)

print("\ntask 1 finished!")
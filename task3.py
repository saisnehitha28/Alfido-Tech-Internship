import pandas as pd
import numpy as np
from datetime import datetime

print("=" * 55)
print("   DATA ANALYSIS WITH PANDAS")
print("   Alfido Tech Internship - Task 3")
print("   Intern: Goudampally Sai Snehitha")
print("=" * 55)

# ============================================================
# PART 1 - CREATE STUDENT DATASET
# ============================================================
print("\nPART 1: CREATING STUDENT DATASET")
print("-" * 40)

# creating student data manually
data = {
    "RollNo":  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name":    ["Snehitha", "Meghana", "Ram", "Teja",
                "Kavya", "Rohith", "Priya", "Arjun",
                "Divya", "Kiran"],
    "Branch":  ["CSE", "ECE", "CSE", "IT",
                "CSE", "MECH", "ECE", "CSE",
                "IT", "MECH"],
    "Python":  [92, 78, 95, 85, 88, 60, 72, 90, None, 65],
    "DSA":     [88, 82, 90, 80, 91, 65, 75, 85, 78, None],
    "DBMS":    [85, 80, 92, 75, 87, 70, 68, 88, 82, 60],
    "Attendance": [95, 88, 92, 85, 90, 70, 75, 98, 80, 65]
}

# creating dataframe
df = pd.DataFrame(data)

# save to csv
df.to_csv("students.csv", index=False)
print("dataset created and saved to students.csv!")
print(f"total students: {len(df)}")
print(f"total columns : {len(df.columns)}")

# ============================================================
# PART 2 - LOAD AND INSPECT DATASET
# ============================================================
print("\nPART 2: LOADING AND INSPECTING DATASET")
print("-" * 40)

# load from csv
df = pd.read_csv("students.csv")

print("\nfirst 5 rows:")
print(df.head())

print("\ndataset info:")
print(f"  rows    : {df.shape[0]}")
print(f"  columns : {df.shape[1]}")
print(f"  columns : {list(df.columns)}")

print("\ndata types:")
print(df.dtypes)

print("\nbasic statistics:")
print(df.describe())

# ============================================================
# PART 3 - CLEAN MISSING DATA
# ============================================================
print("\nPART 3: CLEANING MISSING DATA")
print("-" * 40)

print("missing values before cleaning:")
print(df.isnull().sum())

# fill missing values with column mean
df["Python"] = df["Python"].fillna(
    df["Python"].mean())
df["DSA"] = df["DSA"].fillna(
    df["DSA"].mean())

print("\nmissing values after cleaning:")
print(df.isnull().sum())
print("all missing values filled with column mean!")

# ============================================================
# PART 4 - ADD CALCULATED COLUMNS
# ============================================================
print("\nPART 4: ADDING CALCULATED COLUMNS")
print("-" * 40)

# calculate total marks
df["Total"] = df["Python"] + df["DSA"] + df["DBMS"]

# calculate percentage
df["Percentage"] = round(
    (df["Total"] / 300) * 100, 2)

# assign grades
def get_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Percentage"].apply(get_grade)

# pass or fail based on attendance
df["Status"] = df["Attendance"].apply(
    lambda x: "Pass" if x >= 75 else "Fail")

print("calculated columns added!")
print("\nupdated dataset:")
print(df[["Name", "Total", "Percentage",
          "Grade", "Status"]])

# ============================================================
# PART 5 - FILTERING DATA
# ============================================================
print("\nPART 5: FILTERING DATA")
print("-" * 40)

# filter top students
top_students = df[df["Percentage"] >= 80]
print(f"top students (above 80%):")
for _, row in top_students.iterrows():
    print(f"  {row['Name']} - {row['Percentage']}% - "
          f"Grade {row['Grade']}")

# filter CSE students
cse = df[df["Branch"] == "CSE"]
print(f"\nCSE students: {len(cse)}")
for _, row in cse.iterrows():
    print(f"  {row['Name']} - {row['Percentage']}%")

# filter failed attendance
failed = df[df["Status"] == "Fail"]
print(f"\nstudents with low attendance: {len(failed)}")
for _, row in failed.iterrows():
    print(f"  {row['Name']} - {row['Attendance']}%")

# ============================================================
# PART 6 - GROUPING AND AGGREGATION
# ============================================================
print("\nPART 6: GROUPING AND AGGREGATION")
print("-" * 40)

# group by branch
print("average marks by branch:")
branch_avg = df.groupby("Branch")["Percentage"].mean()
for branch, avg in branch_avg.items():
    print(f"  {branch}: {round(avg, 2)}%")

# group by grade
print("\nstudents per grade:")
grade_count = df.groupby("Grade")["Name"].count()
for grade, count in grade_count.items():
    print(f"  Grade {grade}: {count} students")

# total marks per branch
print("\ntotal marks by branch:")
branch_total = df.groupby("Branch")["Total"].sum()
for branch, total in branch_total.items():
    print(f"  {branch}: {total} marks")

# ============================================================
# PART 7 - IMPORTANT INSIGHTS
# ============================================================
print("\nPART 7: KEY INSIGHTS")
print("-" * 40)

topper = df.loc[df["Percentage"].idxmax()]
lowest = df.loc[df["Percentage"].idxmin()]
avg_pct = round(df["Percentage"].mean(), 2)
avg_attendance = round(df["Attendance"].mean(), 2)
pass_count = len(df[df["Status"] == "Pass"])
fail_count = len(df[df["Status"] == "Fail"])

print(f"class topper     : {topper['Name']} "
      f"({topper['Percentage']}%)")
print(f"lowest scorer    : {lowest['Name']} "
      f"({lowest['Percentage']}%)")
print(f"class average    : {avg_pct}%")
print(f"avg attendance   : {avg_attendance}%")
print(f"students passed  : {pass_count}")
print(f"students failed  : {fail_count}")
print(f"best branch      : "
      f"{branch_avg.idxmax()} "
      f"({round(branch_avg.max(), 2)}%)")

# ============================================================
# PART 8 - SAVE CLEANED DATA
# ============================================================
print("\nPART 8: SAVING CLEANED DATA")
print("-" * 40)

df.to_csv("students_analyzed.csv", index=False)
print("cleaned and analyzed data saved!")
print("file: students_analyzed.csv")

# ============================================================
# PART 9 - INSIGHT SUMMARY
# ============================================================
print("\n" + "=" * 55)
print("   INSIGHT SUMMARY")
print("=" * 55)

insights = [
    f"Total {len(df)} students analyzed",
    f"Class topper is {topper['Name']} with "
    f"{topper['Percentage']}%",
    f"Class average percentage is {avg_pct}%",
    f"CSE branch has {len(cse)} students",
    f"{pass_count} students passed attendance criteria",
    f"{fail_count} students failed attendance criteria",
    f"Best performing branch: {branch_avg.idxmax()}",
    f"2 missing values were filled using column mean",
    f"Grades assigned: A+, A, B, C, D based on percentage"
]

for i, insight in enumerate(insights, 1):
    print(f"  {i}. {insight}")

print("\n" + "=" * 55)
print("   TASK 3 COMPLETED!")
print("=" * 55)
print("   Goudampally Sai Snehitha | BS/REG/120205")
print("   Alfido Tech | Python Developer Intern")
print("=" * 55)
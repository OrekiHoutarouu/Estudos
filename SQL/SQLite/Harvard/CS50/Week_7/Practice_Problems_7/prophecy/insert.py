from cs50 import SQL
import csv

db = SQL("sqlite:///roster.db")
students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

db.execute("INSERT INTO houses (house, head) VALUES ('Gryffindor', 'McGonagall')")
db.execute("INSERT INTO houses (house, head) VALUES ('Slytherin', 'Severus Snape')")
db.execute("INSERT INTO houses (house, head) VALUES ('Ravenclaw', 'Filius Flitwick')")
db.execute("INSERT INTO houses (house, head) VALUES ('Hufflepuff', 'Pomona Sprout')")
db.execute("DELETE FROM houses WHERE id > 4")
houses = db.execute("SELECT * FROM houses")

for student in students:
    db.execute("INSERT INTO students (student_name) VALUES (?)", student["student_name"])
    db.execute("DELETE FROM students WHERE id > 40")

students_names = db.execute("SELECT * FROM students")
student_id = -1;

db.execute("DELETE FROM assignments")
for student in students:
    for student_name in students_names:
        for house_name in houses:
            if student["house"] == house_name["house"] and student["student_name"] == student_name["student_name"]:
                db.execute("INSERT INTO assignments (student_id, house_id) VALUES (?, ?)", student_name["id"], house_name["id"])

assignments = db.execute("SELECT * FROM assignments")
for c in assignments:
    print(c)

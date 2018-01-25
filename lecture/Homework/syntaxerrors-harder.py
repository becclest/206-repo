## syntaxerrors-harder.py

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:
# Charles Dickens died in 1870.
# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens":1870,
    "William Thackeray":1863,
    "Anthony Trollope":1882,
    "Gerard Manley Hopkins":1889
  }

for key, value in authors.items():
  print (key, "died in", value, ".")
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades,
# return an average test score, a corresponding letter grade,
# and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
for grade in grades:
  avg = sum(grades) /(len(grades))
  avg = int(round(avg))


if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Exam: " + str(grade))

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")

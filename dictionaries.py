#A dictionary that converts their scores to grades.
#By the end of your program, you should have a new dictionary called
#student_grades that should contain student names for keys and their grades for values exercise

student_scores = {
  "Harry": 99,
  "Ron": 87,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#Created an empty dictionary called student_grades.

student_grades = {}

#Adding below the grades to student_grades.

for name in student_scores:
  student_grades[name] = student_scores[name]
  
for mark in student_grades:
    if student_scores[mark] > 90:
        student_grades[mark] = "Outstanding"
    if student_scores[mark] > 80 and student_scores[mark] <= 90:
        student_grades[mark] = "Exceeds Expectations"
    if student_scores[mark] > 70 and student_scores[mark] <= 80:
        student_grades[mark] = "Acceptable"
    if student_scores[mark] < 70:
        student_grades[mark] = "Fail"


print(student_grades)

student_scores = {
  "Harry": 99,
  "Ron": 87,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇

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

  
# 🚨 Don't change the code below 👇
print(student_grades)
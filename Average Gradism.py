class Student:
  def __init__(self, first_name, last_name, student_id, age, grade):
    #define initialisation - the first one has been done for you
    self.first_name = first_name
    self.last_name = last_name
    self.student_id = student_id
    self.age = age
    self.grade = {}
    #create an array to store the courses
    self.courses = []
    self.attendance = {}

  #function for course enrolled
  def course_enrollment(self, course):
    self.courses.append(course)

  #function for calculating the total grades. this should return the average grade
  def calculate_average_grade(self):
    total_grades = sum(self.grade.values())
    return total_grades / len(self.grade)

  #function for recording the attendance
  def record_attendance(self, course, attendance):
    self.attendance[course] = attendance

class Course:
  def __init__(self, course_name, course_id):
    #define initialisation - the first one has been done for you
    self.course_name = course_name
    self.course_id = course_id
    self.students = []
    self.grades = {}

  # function to add students
  def add_student(self, student):
    self.students.append(student)
    student.course_enrollment(self)

  #function to add grades
  def assign_grade(self, student, grade):
    self.grades[student] = grade
    student.grade[self.course_name] = grade

student1 = Student("Alice", "Smith", "S123509", 17, 88)
student2 = Student("Bob", "Taylor", "S124500", 18, 90)
course1 = Course("L3 IT", "Data")
course2 = Course("T Level DPDD", "Software")

course1.add_student(student1)
course1.add_student(student2)
course1.assign_grade(student1, 95)
course1.assign_grade(student2, 85)
course1.assign_grade(student1, 93)
student1.record_attendance(course1, True)
student1.record_attendance(course2, False)
average_grade = student1.calculate_average_grade()
if average_grade is not None:
    print("Average grade for", student1.first_name, ":", average_grade)
else:
    print(student1.first_name, "has no recorded grades yet.")
average_grade = student2.calculate_average_grade()
if average_grade is not None:
    print("Average grade for", student2.first_name, ":", average_grade)
else:
    print(student2.first_name, "has no recorded grades yet.")
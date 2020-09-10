from os.path import abspath, dirname, join
from sys import argv

from ..two_dimension_array import TwoDimensionArray

grade_file = open(join(dirname(abspath(argv[0])), "grade_file.txt"))

exams = grade_file.readlines()
students_number = len(exams[0].split())
exams_number = len(exams)
all_grades = TwoDimensionArray(exams_number, students_number)

for exam_index, exam in enumerate(exams):
    for student_index, student_grade in enumerate(exam.split()):
        all_grades[exam_index, student_index] = int(student_grade)
grade_file.close()

for student_index in range(students_number):
    grades_sum = 0
    for exam_index in range(exams_number):
        grades_sum += all_grades[exam_index, student_index]
    print(f"student: {student_index + 1}, average grade: {grades_sum / exams_number}")

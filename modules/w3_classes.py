import csv, random

grades = [0, 2, 4, 7, 10, 12]

class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        count = 0
        total = 0
        rounded_avgs = []
        for course in self.data_sheet.courses:
            count += 1
            total += course.grade

        avg = total / count
        actual_grade = min(grades, key = lambda x: abs(x-avg))
        return actual_grade

    def get_study_progression(self):
        ects_from_5sem = 150
        total = 0
        for course in self.data_sheet.courses:
            if course.grade > 0:
                total += course.ECTS
        
        if total > 150:
            total = 150

        completion_percentage = (total/ects_from_5sem) * 100
        return completion_percentage

    def get_courses(self):
        return self.data_sheet.courses


class DataSheet:
    def __init__(self, courses):
        self.courses = courses

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            if course.grade == -3:
                grades.append(course.ECTS)
            else:
                grades.append({"ECTS": course.ECTS, "grade": course.grade})

        return grades

    def __iter__(self):
        for course in self.courses:
            yield course


class Course:
    def __init__(self, name, classroom, teacher, ECTS, grade=-3):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade


def read_students_from_csv(csv_path):
    cur_student = {}
    students = []
    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        stud_list = list(reader)
        stud_list.pop(0)
        for student in stud_list:
            if hasattr(cur_student, "name") and cur_student.name == student[0]:
                course = Course(student[2], student[5], student[3], int(student[4]), int(student[6]))
                stud_idx = students.index(cur_student)
                students[stud_idx].data_sheet.courses.append(course)
            else:
                courses = []
                courses.append(Course(student[2], student[5], student[3], int(student[4]), int(student[6])))
                data_sheet = DataSheet(courses)
                cur_student = Student(student[0], student[1], data_sheet, student[7])
                students.append(cur_student)
    
    return students
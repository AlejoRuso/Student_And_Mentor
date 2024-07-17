def __lt__(self, other):
    return self.grades < other.gredes

def __eq__(self, other):
    return self.grade == other.grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress or course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
        
    def average_grade(self):
        grade_count = 0
        grade_sum = 0
        for i in self.grades:
            for x in self.grades[i]:
                grade_sum += x
                grade_count += 1
        if grade_count == 0:
            return 0
        else:
            return grade_sum / grade_count
    
    
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')  
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def average_grade(self):
        grade_count = 0
        grade_sum = 0
        for i in self.grades:
            for x in self.grades[i]:
                grade_sum += x
                grade_count += 1
        if grade_count == 0:
            return 0
        else:
            return grade_sum / grade_count         
        
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}')         
        
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade = {}
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')        
    

lecturer1 = Lecturer('Олег', 'Булыгин')
lecturer1.courses_attached = ['Python', 'OOP']

lecturer2 = Lecturer('Елена', 'Никитина')
lecturer2.courses_attached = ['Python','OOP']
        
student1 = Student('Иванов', 'Иван', 'мужской')
student1.courses_in_progress += ['OOP']
student1.finished_courses += ['Python']
student1.rate_lecturer(lecturer1,'Python',10)
student1.rate_lecturer(lecturer2,'Python',8)

student2 = Student('Сидоров', 'Петр', 'мужской')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['OOP']
student2.rate_lecturer(lecturer1,'Python',10)
student2.rate_lecturer(lecturer2,'Python',9)


reviewer1 = Reviewer('Батицкая', 'Алена')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['OOP']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'OOP', 5)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'OOP', 8)

reviewer2 = Reviewer('Петрова', 'Мария')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['OOP']
reviewer2.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student1, 'OOP', 5)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'OOP', 10)





print('Студенты:')
print(student1)
print(student2)
print('')
print('Проверяющие:')
print(reviewer1)
print(reviewer2)
print('')
print('Лекторы:')
print(lecturer1)
print(lecturer2)
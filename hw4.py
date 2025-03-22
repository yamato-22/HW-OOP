class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [self._true_grade(grade)]
            else:
                lecturer.grades[course] = [self._true_grade(grade)]
        else:
            return 'Ошибка'

    def _true_grade(self, grade):
        if grade > 10:
            return 10
        elif grade < 1:
            return 1
        else:
            return grade

    def _mean_score(self):
        summ = 0
        count = 0
        for grade in self.grades.values():
            summ += sum(grade)
            count += len(grade)
        # return sum(sum(d) / len(d) for d in self.grades.values()) / len(self.grades)
        return summ / count

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {round(self._mean_score(), 1)} \n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._mean_score() == other._mean_score()
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Student):
            return self._mean_score() != other._mean_score()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._mean_score() < other._mean_score()
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self._mean_score() > other._mean_score()
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self._mean_score() <= other._mean_score()
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self._mean_score() >= other._mean_score()
        else:
            return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _mean_score(self):
        summ = 0
        count = 0
        for grade in self.grades.values():
            summ += sum(grade)
            count += len(grade)
        return summ / count

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {round(self._mean_score(), 1)}')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._mean_score() == other._mean_score()
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self._mean_score() != other._mean_score()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._mean_score() < other._mean_score()
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self._mean_score() > other._mean_score()
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self._mean_score() <= other._mean_score()
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self._mean_score() >= other._mean_score()
        else:
            return False


class Reviewers(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


def averange_grade_students(students, course):
    summ = 0
    count = 0
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                summ += sum(value)
                count += len(value)
    if count == 0:
        return 0
    else:
        return round(summ / count, 1)

def averange_grade_lecturers(lecturers, course):
    summ = 0
    count = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                summ += sum(value)
                count += len(value)
    if count == 0:
        return 0
    else:
        return round(summ / count, 1)

# Create Students
student1 = Student('Ivan', 'Ivanov', 'male')
student1.courses_in_progress = ['Python','Java']
student1.finished_courses = ['Fortran']

student2 = Student('Ivan', 'Smirnov', 'male')
student2.courses_in_progress = ['Java','Assembler']
student2.finished_courses = ['Fortran']

# Create Lecturer
lecturer1 = Lecturer('Egor', 'Egorov')
lecturer1.courses_attached = ['Python','Java']

lecturer2 = Lecturer('Egor', 'Fedorov')
lecturer2.courses_attached = ['Assembler','Java']

# Create Reviewers
reviewer1 = Reviewers('Petr', 'Petrov')
reviewer1.courses_attached = ['Python']
reviewer2 = Reviewers('Yurii', 'Petrov')
reviewer2.courses_attached = ['Java']

#Проверяющие оценивают студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer2.rate_hw(student1, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 6)
reviewer2.rate_hw(student2, 'Java', 8)

# Лекторы получают оценки от студентов за лекции
student1.rate_lecturer(lecturer1, 'Python', 6)
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Java', 10)

student2.rate_lecturer(lecturer2, 'Java', 8)
student2.rate_lecturer(lecturer2, 'Java', 4)

print('Проверяющий №1')
print(reviewer1)
print('Проверяющий №1')
print(reviewer2)
print('Студент №1')
print(student1)
print('Студент №2')
print(student2)
print('Лектор №1')
print(lecturer1)
print('Лектор №2')
print(lecturer2)

# Сравниваем лекторов
print(f'Лектор №1 == Лектор №2, результат: {lecturer1 == lecturer2}')
print(f'Лектор №1 > Лектор №2, результат: {lecturer1 > lecturer2}')
print(f'Лектор №1 < Лектор №2, результат: {lecturer1 < lecturer2}')
print(f'Лектор №1 != Лектор №2, результат: {lecturer1 != lecturer2}')
print(f'Лектор №1 >= Лектор №2, результат: {lecturer1 >= lecturer2}')
print(f'Лектор №1 <= Лектор №2, результат: {lecturer1 <= lecturer2}')

# Сравниваем студентов
print(f'Студент №1 == Студент №2, результат: {student1 == student2}')
print(f'Студент №1 > Студент №2, результат: {student1 > student2}')
print(f'Студент №1 < Студент №2, результат: {student1 < student2}')
print(f'Студент №1 != Студент №2, результат: {student1 != student2}')
print(f'Студент №1 >= Студент №2, результат: {student1 >= student2}')
print(f'Студент №1 <= Студент №2, результат: {student1 == student2}')

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]
course_name = 'Java'
print(f'Средняя оценка всех студентов за курс {course_name} = {averange_grade_students(students_list, course_name)}')
print(f'Средняя оценка всех преподавателей по предмету {course_name} = {averange_grade_lecturers(lecturers_list, course_name)}')
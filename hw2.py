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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


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



# student1 = Student('Ivan', "Ivanov", 'male')
# student1.courses_in_progress = ['Python']
# lecturer1 = Lecturer('Egor', 'Egorov')
# lecturer1.courses_attached = ['Python']
# reviewer1 = Reviewers('Peter', 'Petrov')
# reviewer1.courses_attached = ['Python']
# reviewer1.rate_hw(student1, 'Python', 10)
# reviewer1.rate_hw(student1, 'Python', 5)
# print(student1.grades)
# student1.rate_lecturer(lecturer1, 'Python', 15)
# print(f'Преподаватель {lecturer1.name} {lecturer1.surname} имеет следующие отзывы {lecturer1.grades}')
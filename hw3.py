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
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: " \
               f"{self.average_grade}\nКурсы в процессе изучения: " \
               f"{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}  "

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        pass


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._marked = {}
        self._average_mark = 0
    def mark_by_student(self, student, course, grade):
        if isinstance(self, Lecturer) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= grade <= 10:
                if course in self._marked:
                    self._marked[course].append(grade)
                else:
                    self._marked[course] = [grade]
                summa, lena = 0, 0
                for i in self._marked:
                    summa = sum(self._marked[i]) + summa
                    lena = len(self._marked[i]) + lena
                self._average_mark = summa / lena

    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nСредняя оценка за лекции: {self._average_mark} "

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            summa, lena = 0, 0
            for i in student.grades:
                summa = sum(student.grades[i]) + summa
                lena = len(student.grades[i]) + lena
            student.average_grade = summa / lena
        else:
            return 'Ошибка'
    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}"

def compare_lectures(lecture1, lecture2):
    if lecture1._average_mark > lecture2._average_mark:
        print(lecture1.surname + ' ' + lecture1.name, 'имеет больший средний балл по сравнению с ', lecture2.surname
              + ' ' + lecture2.name)
    elif lecture1._average_mark < lecture2._average_mark:
        print(lecture2.surname + ' ' + lecture2.name, 'имеет больший средний балл по сравнению с ', lecture1.surname +
              ' ' + lecture1.name)
    elif lecture1._average_mark == lecture2._average_mark:
        print('Средний балл одинаков')

def compare_students(student1, student2):
    if student1._average_grade > student2._average_grade:
        print(student1.surname + ' ' + student1.name, 'имеет больший средний балл по сравнению с ', student2.surname +
              ' ' + student2.name)
    elif student1._average_grade < student2._average_grade:
        print(student2.surname + ' ' + student2.name, 'имеет больший средний балл по сравнению с ', student1.surname +
              ' ' + student1.name)
    elif student1._average_grade == student2._average_grade:
        print('Средний балл одинаков')

def average_students_marks_in_course(students_list, course):
    summa, lena = 0, 0
    for i in students_list:
        if course in i.courses_in_progress:
            summa = sum(i.grades[course]) + summa
            lena = len(i.grades[course]) + lena
    print('Средняя оценка студентов за курс', summa/lena)

def average_lectures_marks_in_course(lectures_list, course):
    summa, lena = 0, 0
    for i in lectures_list:
        if course in i.courses_attached:
            summa = sum(i._marked[course]) + summa
            lena = len(i._marked[course]) + lena
    print('Средняя оценка лекторов за курс', summa/lena)

best_student = Student('Иван', 'Иванов', 'мужской')
best_student2 = Student('Ольга', 'Васильева', 'женский')
best_student.courses_in_progress.append('Python')
best_student.courses_in_progress.append('Math')
best_student2.courses_in_progress.append('Python')
best_student2.courses_in_progress.append('Math')

lecture = Lecturer('Николай', 'Валяйкин')
lecture2 = Lecturer('Анастасия', 'Крылова')
lecture.courses_attached.append('Python')
lecture2.courses_attached.append('Python')
lecture2.courses_attached.append('Math')

rewiever = Reviewer('Денис', 'Морозов')
rewiever2 = Reviewer('Александр', 'Афанасьев')
rewiever.courses_attached.append('Python')
rewiever.courses_attached.append('Math')
rewiever2.courses_attached.append('Math')

lecture.mark_by_student(best_student, 'Python', 6)
lecture.mark_by_student(best_student2, 'Python', 4)
lecture2.mark_by_student(best_student2, 'Python', 8)
lecture2.mark_by_student(best_student2, 'Python', 10)
lecture2.mark_by_student(best_student2, 'Math', 4)
lecture2.mark_by_student(best_student2, 'Math', 7)

rewiever.rate_hw(best_student, 'Python', 6)
rewiever.rate_hw(best_student, 'Python', 8)
rewiever.rate_hw(best_student, 'Math', 5)
rewiever.rate_hw(best_student2, 'Python', 9)
rewiever.rate_hw(best_student2, 'Math', 1)
rewiever.rate_hw(best_student2, 'Math', 4)

stud_list = [best_student, best_student2]
lectures_list = [lecture, lecture2]

print(best_student.grades)
print(best_student2.grades)

average_students_marks_in_course(stud_list, 'Python')
average_lectures_marks_in_course(lectures_list, 'Python')
print(best_student)
print(lecture)
print(rewiever)

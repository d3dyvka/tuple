#1 задача
def tpl_sort(a):
    for i in a:
        if not isinstance(i, int):
            return a
    return sorted(a)


print(tpl_sort((2, 7, 9, 10, 38, 324, 326, 767, 22, 57, 942)))


#2 задача
def slicer(a, elem):
    if elem in a:
        if a.count(elem) > 1:
            first = a.index(elem)
            second = a.index(elem, first + 1) + 1
            return a[first:second]
        else:
            return a[a.index(elem):]
    else:
        return ()


print(slicer((2, 7, 9, 10, 38, 324, 326, 767, 22, 57, 942), 7))


#3 задача
def sieve(lst):
    a = []
    lst = lst[::-1]
    for i in lst:
        if i not in a:
            a.append(i)
    return a

print(sieve((1, 2, 3, 3, 2)))


#4 задача
def del_from_tuple(krt, elem):
    lst_from_krt = list(krt)
    if elem in lst_from_krt:
        lst_from_krt.remove(elem)
        return lst_from_krt
    else:
        return krt

print(del_from_tuple((1, 2, 3), 3))


#5 задача
from collections import namedtuple
Student = namedtuple('Student', 'name age mark city')
students = (
    Student('Иван', '17', 4.5, 'Новосибирск'),
    Student('Максим', '18', 4.2, 'Москва'),
    Student('Игорь', '15', 3.2, 'Ульяновск'),
    Student('Ульяна', '19', 3.5, 'Санкт-Петербург'),
    Student('Ирина', '17', 4.0, 'Уфа'),
    Student('Тунай', '20', 3.8, 'Железногорск'),
    Student('Зерно', '16', 3.1, 'Гринландия')
)
def good_students(students):
    names = []
    a = 0
    for i in students:
        a += i.mark
    all = a / len(students)

    for student in students:
        if student.mark >= all:
            names.append(student.name)

    print('Ученики', ', '.join(names), 'в этом семестре хорошо учатся!')

good_students(students)

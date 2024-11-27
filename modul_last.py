grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]
          ]                                                          # sum/len
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}        # список в алфавитном порядке

sort_students = list(students)
sort_students.sort()

average_grade = [
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4])
]

# print(students)
# print(grade)
# print(average_grade)



# print(sort_students)

                                                     # составить словарь

mark_list = {}

b = average_grade[0]
a = sort_students[0]
mark_list.update({ a : b })

b = average_grade[1]
a = sort_students[1]
mark_list.update({ a : b })

b = average_grade[2]
a = sort_students[2]
mark_list.update({ a : b })

b = average_grade[3]
a = sort_students[3]
mark_list.update({ a : b })

b = average_grade[4]
a = sort_students[4]
mark_list.update({ a : b })

print(mark_list)

# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_list = len(my_list)
int = 0

while int < len_list:
    if my_list[int] < 0:
        break
    if my_list[int] == 0:
        int += 1
        continue
    print(my_list[int])
    int += 1

print('Всё!')
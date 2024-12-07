import random

num = random.randint(3, 20)
print(num)

num_list1 = list(range(1, num))
num_list2 = list(range(1, num))
password =  []

for i in num_list1:
    for j in num_list2:
        if num % (i + j) == 0:
            if i == j:
                continue
            password.append(i)
            password.append(j)
    num_list2.remove(i)
    # print("List2:", num_list2)

print("Наш пароль: ", *password)

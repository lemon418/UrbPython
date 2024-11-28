first = input('Enter 1st num: ')
second = input('Enter 2nd num: ')
third = input('Enter 3d2 num: ')

if first == second == third :
    print(3)
elif first == second or second == third or third == first :
    print(2)
else:
    print(0)
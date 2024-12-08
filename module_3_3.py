def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params('Один')
print_params(1, 'тетрадь', False)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])

value_list = [ 1, True, 'str']
values_dict = { 'a': 2, 'b': 'One', 'c': False}

print_params(*value_list)
print_params(**values_dict)

values_list_2 = [True, 1]
print_params(*values_list_2, 42)
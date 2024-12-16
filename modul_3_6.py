data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

count = 0

def summ_(*object):
    global count

    for el in object:

        if isinstance(el, int):
            count += el

        if isinstance(el, str):
            count += len(el)

        if  isinstance(el, tuple | set | list):
            summ_(*el)

        if isinstance(el, dict):
            for i in el:
                count += len(i)
                count += el[i]

    return count

print(summ_(*data_structure))

my_dict = { 'pepsi': 100,
            'coca-cola' : 80,
            'fanta': 95
            }

print('Price list: ',my_dict)

print('Existing value: ' ,my_dict.get('coca-cola'))
print('Not existing value: ', my_dict.get('sprite'))

my_dict.update({ 'sprite': 80,
                 '7up': 85
                 })

pepsi = my_dict.pop('pepsi')
print('Deleted value: ', pepsi)

print('New_price_list: ', my_dict)


my_set = {6, 2, 3, 4, 2, 4, 'Nike', 'Adidas', 'Nike'}
print('Set: ', my_set)

my_set.add('Puma')
my_set.add(True)
my_set.discard('Nike')
print('Modified set:  ', my_set)
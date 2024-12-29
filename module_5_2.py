class House():
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor):
        if (self.numbers_of_floor < new_floor) or (new_floor < 1):
            print('Такого этажа не существует')

        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.numbers_of_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numbers_of_floor}"


hotel = House('Hotel', 18)
yalta = House('ЖК "Yalta"', 20)

print(len(hotel))
print(len(yalta))

print(str(hotel))
print(str(yalta))
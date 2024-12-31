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

    def __eq__(self, other):
        return self.numbers_of_floor == other.numbers_of_floor

    def __lt__(self, other):
        return self.numbers_of_floor < other.numbers_of_floor

    def __le__(self, other):
        return self.numbers_of_floor <= other.numbers_of_floor

    def __gt__(self, other):
        return self.numbers_of_floor > other.numbers_of_floor

    def __ge__(self, other):
        return self.numbers_of_floor >= other.numbers_of_floor

    def __ne__(self, other):
        return self.numbers_of_floor != other.numbers_of_floor

    def __add__(self, value):
        self.numbers_of_floor += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

hotel = House('Hotel', 10)
yalta = House('ЖК "Yalta"', 20)

print(hotel)
print(yalta)

print(hotel == yalta)

hotel = hotel + 10 # __add__
print(hotel)
print(hotel == yalta)

hotel += 10
print(hotel)

yalta = 10 + yalta
print(hotel)

print(hotel > yalta)
print(hotel >= yalta)
print(hotel < yalta)
print(hotel <= yalta)
print(hotel != yalta)
class House():
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = int(numbers_of_floor)

    def go_to(self, new_floor):
        if (self.numbers_of_floor < new_floor) or (new_floor < 1):
            print('Такого этажа не существует')

        else:
            for i in range(1, new_floor + 1):
                print(i)

yalta = House('ЖК "Yalta"', 20)
yalta.go_to(21)

hotel = House('Hotel', 18)
yalta.go_to(5)

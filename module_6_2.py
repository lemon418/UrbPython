class Vehicle():
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

        if self.__color not in self.__COLOR_VARIANTS:
            print("Таких цветов в каталоге нет")
            exit()

    def get_horsepower(self):
                return(f"Модель: {self.__engine_power}")

    def get_color(self):
                return(f"Цвет: {self.__color}")

    def print_info(self):
                print(self.owner)
                print(self.__model)
                print(self.get_horsepower())
                print(self.get_color())

    def set_color(self, new_color):
                self.__color = new_color

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()



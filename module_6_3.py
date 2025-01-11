import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = int(speed)
    def move(self, dx, dy, dz):
        int(dx)
        if dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords = [dx*self.speed, dy*self.speed, dz*self.speed]

    def get_cords(self):
        print( f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {int(self._cords[2])}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("I'm peacfull ;)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be carefull, I'm attacking you!")
    def speak(self):
        print(self.sound)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Bird(Animal):
    beak = True
    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        eggs_ = random.randint (0,4)
        print(f"Here are(is) {eggs_} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    def dive_in(self, dz):
         dive = abs(dz)*self.speed/2
         self._cords[2] = self._cords[2] - dive

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
db.move(1, 4,  -1)
db.get_cords()
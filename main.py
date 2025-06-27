

class Bmw:
    def see_weelhs(self):
        print("Diski m5f90")

    def see_doors(self):
        print("Dveri mka bambino")


class Audi:
    def see_weelhs(self):
        print("Diski audiii")

    def see_doors(self):
        print("Dveri audushka")


class Opel:
    def see_weelhs(self):
        print("Diski opelek")

    def see_doors(self):
        print("Dveri opelichka")


class Car:
    def see_doors(self, car):
        car.see_weelhs()
        show_doors = car.see_doors()
        return show_doors




class Animal:
    def voice(self):
        print("Voiceee")


class Dog(Animal):
    def voice(self):
        print("GAvv GAvvv")

class Cat(Animal):
    def voice(self):
        print("Miioooyya")

def do_voise(animal: Animal):
    animal.voice()


class Geometric:
    def __init__(self,a ,b):
        self.a = a
        self.b = b

    def calc(self):
        return self.a + self.b



first = Geometric(5,6)
print(first.calc())
tom = Cat()
do_voise(tom)




bmw = Car()
bmw.see_doors(Opel())





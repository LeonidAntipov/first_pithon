

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


bmw = Car()
bmw.see_doors(Opel())





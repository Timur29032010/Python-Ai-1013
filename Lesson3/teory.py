class Human:
    def __init__(self,name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand="BMW"):
        self.brand = brand
        self.passengers =[]
    def add_passengers(self,human):
        self.passengers.append(human)
    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of{self.brand}")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in{self.brand}")

nick = Human("Nick")
kate = Human ("Kate")
Borys = Human()
car = Auto("Bmw")
car.add_passengers(nick)
car.add_passengers(kate)
car.add_passengers(Borys)
car.print_passengers_names()


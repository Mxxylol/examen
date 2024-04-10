class Animal:
    def __init__(self, specie, an):
        self.specia = specie
        self.an = an

class Caine(Animal):
    def __init__(self, specie, an, rasa):
        self.rasa = rasa
        super().__init__(specie, an)

    def sunet(self):
        self.suneet = "ham-ham"
        return self.suneet

caine = Caine("Caine", 1, "Sasisca")
print(caine.specia, caine.an, caine.rasa, caine.sunet())




class Calculator:
    def __init__(self, nr1, nr2):
        self.nr1 = nr1
        self.nr2 = nr2
        try:
            print(float(nr1/nr2))
        except TypeError:
            print("GRESIT")
        except ZeroDivisionError:
            print(" la 0 bu poti imparti!!!!!!!!?!?!?!")
        else:
            print("haros")

calculator = Calculator(0, 0)
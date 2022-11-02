import random


class Karta(object):
    figura = ['AS', 'KROL', 'DAMA', 'JOPEK', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    kolor = ['kier', 'pik', 'karo', 'trefl']

    def __init__(self, figura, kolor):
        self.figura = figura
        self.kolor = kolor

    def __str__(self) -> str:
        x = self.figura + "-" + self.kolor
        return x


class Gracz(object):

    def __init__(self):
        self.karty = []

    def __str__(self):
        if self.karty:
            reka = ""
            for karty in self.karty:
                reka += str(karty) + " "
        else:
            reka = "Pusta"
        return reka

    def add(self, karta):
        self.karty.append(karta)

    def give(self, karta, inny_gracz):
        self.karty.remove(karta)
        inny_gracz.add(karta)


class Talia(Gracz):

    def talia(self):
        for kolor in Karta.kolor:
            for figura in Karta.figura:
                self.add(Karta(figura, kolor))

    def tasowanie(self):
        random.shuffle(self.karty)

    def rozdawanie(self, gracze, ile_kart):
        for x in range(ile_kart):
            for y in gracze:
                if self.karty:
                    pierwsza = self.karty[0]
                    self.give(pierwsza, y)
                else:
                    print("brak kart")


talia1 = Talia()
talia1.talia()
print("____________________________________")
print(talia1)
talia1.tasowanie()
print("____________________________________")
print(talia1)

karty1 = Gracz()
karty2 = Gracz()
gracze = [karty1, karty2]

talia1.rozdawanie(gracze, 5)
print("____________________________________")
print(karty1)
print("____________________________________")
print(karty2)

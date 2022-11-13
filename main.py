import numpy as np
import os


class map:
    def __init__(self, columns, rows):
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.map = np.full((rows, columns), '.', str)

    def setStart(self, value_x, value_y):
        self.start_x = value_x
        self.start_y = value_y
        self.map[self.start_y][self.start_x] = 'S'

    def setEnd(self, value_x, value_y):
        self.end_x = value_x
        self.end_y = value_y
        self.map[self.end_y][self.end_x] = 'E'

    def clearPosition(self, player):
        self.map[player.current_y][player.current_x] = '.'

    def updatePosition(self, player):
        self.map[player.current_y][player.current_x] = 'P'

    def __str__(self) -> str:
        return str(self.map)


class player:
    def __init__(self, start_x, start_y) -> None:
        self.current_x = start_x
        self.current_y = start_y

    def changeOfPosition(self, direction):
        if direction == "W" or direction == 'w':
            if self.current_y >= 1:
                self.current_y -= 1
        elif direction == "S" or direction == 's':
            if self.current_y <= 3:
                self.current_y += 1
        elif direction == "A" or direction == 'a':
            if self.current_x >= 1:
                self.current_x -= 1
        elif direction == "D" or direction == 'd':
            if self.current_x <= 3:
                self.current_x += 1


mapa = map(5, 5)
mapa.setStart(0, 0)
mapa.setEnd(4, 4)
bob = player(mapa.start_x, mapa.start_y)

while bob.current_x != mapa.end_x or bob.current_y != mapa.end_y:
    os.system('cls')
    print(mapa)
    direction = input("W którym kierunku chcesz sie poruszyc?: ")
    mapa.clearPosition(bob)
    bob.changeOfPosition(direction)
    mapa.updatePosition(bob)
print("Gra zakończona, koniec zdobyty! Brawo!")

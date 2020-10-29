import random

desk = [['O' for i in range(6)] for j in range(6)]
desk_comp = [['O' for i in range(6)] for j in range(6)]
desk_player = [['O' for i in range(6)] for j in range(6)]
desk_pole = [['O' for i in range(6)] for j in range(6)]


class Desk:

    def __init__(self, name, desk, *ships):
        self.name = name
        self.ships = ships
        self.desk = desk

    @property
    def getDesk(self):
        return self.desk

    @property
    def getShips(self):
        return self.ships

    def setShips(self, *args, i=0):
        while len(args[0]) != i:
            if self.desk[args[0][i][0]][args[0][i][1]] == "O":
                self.desk[args[0][i][0]][args[0][i][1]] = "■"
                i += 1
                self.setShips(*args, i)
            else:
                return
        return self.desk

    @property
    def getDecor(self):
        return [print(' | ', a, ' | ', b, ' | ', c, ' | ', d, ' | ', e, ' | ', f, ' | ') for a, b, c, d, e, f in
                self.desk]


class Ship:
    _coords = []

    def __init__(self, coords):
        self._coords = coords

    @property
    def coords(self):
        return self._coords


ship_3 = Ship([[3, 3], [4, 3], [5, 3]])  # трехпалубный
ship2_1, ship2_2 = Ship([[0, 0], [0, 1]]), Ship([[5, 5], [4, 5]])  # двухпалубный
ship1_1, ship1_2, ship1_3, ship1_4 = Ship([5, 0]), Ship([0, 5]), Ship([2, 1]), Ship([2, 5])  # однопалубный
flot = *ship_3.coords, *ship2_1.coords, *ship2_2.coords, ship1_1.coords, ship1_2.coords, ship1_3.coords, ship1_4.coords  # флотилия
flot_comp = [4, 1], [4, 2], [4, 3], [3, 5], [2, 5], [2, 0], [2, 1], [0, 1], [0, 3], [0, 5], [5, 5]
comp = Desk('comp', desk_comp, flot_comp)  # доска комп
comp.setShips(flot_comp)
player = Desk('player', desk_player, flot)  # доска игрок
player.setShips(*player.getShips)
battlefield = Desk('battlefield', desk_pole)

print()


def compShot():
    xc, yc = random.randint(0, 5), random.randint(0, 5)
    if not "■" in set(str(player.getDesk)):
        return print("COMPS WIN")
    elif player.getDesk[xc][yc] == "O":
        player.getDesk[xc][yc] = "T"
    elif player.getDesk[xc][yc] == "■":
        compShot()
        player.getDesk[xc][yc] = "X"
    elif player.getDesk[xc][yc] == "T":
        compShot()
    return


def play():  # GAME START
    battlefield.getDecor  # поле вражеское
    print('---------------------------------------')
    player.getDecor  # поле игрока
    try:
        x = "%02d" % (int(input("SHOOT (xy)|(11-66) : ")) - 11)
    except IndexError as ie:
        print(ie)
    y_1, y_2 = int(x[0]), int(x[1])
    if not "■" in set(str(comp.getDesk)):
        return print("PLAYERS WIN")
    elif comp.getDesk[y_1][y_2] == "O":
        comp.getDesk[y_1][y_2] = "T"
        battlefield.getDesk[y_1][y_2] = "T"
        compShot()  # comp shoot
        play()
    elif comp.getDesk[y_1][y_2] == "■":
        comp.getDesk[y_1][y_2] = "X"
        battlefield.getDesk[y_1][y_2] = "X"
        play()
    elif comp.getDesk[y_1][y_2] == "T":
        raise ValueError("Нельзя попасть в одну и ту же клетку дважды")
        # play()


play()

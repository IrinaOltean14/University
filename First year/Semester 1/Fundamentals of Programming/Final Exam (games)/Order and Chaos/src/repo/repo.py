from texttable import Texttable


class Board:
    def __init__(self):
        self._height = 6
        self._width = 6
        self._data = [[' ' for i in range(self._width)] for j in range(self._height)]

    def __str__(self):
        t = Texttable()
        header = []
        for i in range(0, 6):
            header.append(str(i))
        t.header(header + ['/'])
        for i in range(0, self._height):
            t.add_row(self._data[i] + [str(i)])
        return t.draw()

    def return_data(self):
        return self._data

    def move_order(self, row, column, symbol):
        self._data[row][column] = symbol

    def remove_move(self, i, j):
        self._data[i][j] = ' '





class Service:
    def __init__(self, repo):
        self._repo = repo
        self._moves = 0

    def display_board(self):
        return self._repo

    def verify_move(self, row, column, symbol):
        row = str(row)
        column = str(column)
        if symbol != '0' and symbol != 'X':
            return False
        if row < '0' or row > '5' or column < '0' or column > '5':
            return False
        row = int(row)
        column = int(column)
        data = self._repo.return_data()
        if data[row][column] != ' ':
            return False
        return True

    def move_order(self, row, column, symbol):
        self._repo.move_order(row, column, symbol)
        self._moves += 1

    def check_win_status_chaos(self):
        if self._moves == 36:
            return True
        return False

    def check_win_status_order(self):
        data = self._repo.return_data()
        for i in range(0,6):
            for j in range(0,6):
                if data[i][j] != ' ':
                    symbols = 1
                    i1 = i-1
                    while i1 >= 0 and data[i1][j] == data[i][j]:
                        symbols += 1
                        i1 -= 1
                    i1 = i+1
                    while i1 <= 5 and data [i1][j] == data[i][j]:
                        symbols += 1
                        i1+= 1
                    if symbols >=4:
                        return True
                    symbols = 1
                    j1 = j-1
                    while j1 >= 0 and data[i][j1] == data[i][j]:
                        symbols += 1
                        j1 -= 1
                    j1 = j+1
                    while j1 <= 5 and data [i][j1] == data[i][j]:
                        symbols += 1
                        j1+= 1
                    if symbols >=4:
                        return True

                    symbols = 1
                    i1 = i-1
                    j1 = j-1
                    while i1 >= 0 and j1>=0 and data[i1][j1] == data[i][j]:
                        symbols += 1
                        i1 -= 1
                        j1 -= 1
                    i1 = i+1
                    j1 = j+1
                    while i1 <= 5 and j1 <= 5 and data[i1][j1] == data[i][j]:
                        symbols += 1
                        i1+= 1
                        j1+=1
                    if symbols >=4:
                        return True

                    symbols = 1
                    i1 = i - 1
                    j1 = j + 1
                    while i1 >= 0 and j1 <= 5 and data[i1][j1] == data[i][j]:
                        symbols += 1
                        i1 -= 1
                        j1 += 1
                    i1 = i + 1
                    j1 = j - 1
                    while i1 <= 5 and j1 >= 0 and data[i1][j1] == data[i][j]:
                        symbols += 1
                        i1 += 1
                        j1 -= 1
                    if symbols >= 4:
                        return True
        return False


    def check_win_possibility(self):
        data = self._repo.return_data()
        for i in range(0, 6):
            for j in range(0, 6):
                if data[i][j] != ' ':
                    if data[i][j] == '0':
                        ret_symbol = 'X'
                    else:
                        ret_symbol = '0'
                    symbols = 1
                    i1 = i - 1
                    while i1 >= 0 and data[i1][j] == data[i][j]:
                        symbols += 1
                        i1 -= 1
                    i2 = i + 1
                    while i2 <= 5 and data[i2][j] == data[i][j]:
                        symbols += 1
                        i2 += 1
                    if symbols >= 3:
                        if i1 >= 0 and self.verify_move(i1,j,ret_symbol):
                            return i1, j, ret_symbol
                        if i2 <= 5 and self.verify_move(i2,j, ret_symbol):
                            return i2, j, ret_symbol
                    symbols = 1
                    j1 = j - 1
                    while j1 >= 0 and data[i][j1] == data[i][j]:
                        symbols += 1
                        j1 -= 1
                    j2 = j + 1
                    while j2 <= 5 and data[i][j2] == data[i][j]:
                        symbols += 1
                        j2 += 1
                    if symbols >= 3:
                        if j1 >= 0 and self.verify_move(i,j1, ret_symbol):
                            return i, j1, ret_symbol
                        if j2 <= 5 and self.verify_move(i,j2,ret_symbol):
                            return i, j2, ret_symbol

                    symbols = 1
                    i1 = i - 1
                    j1 = j - 1
                    while i1 >= 0 and j1 >= 0 and data[i1][j1] == data[i][j]:
                        symbols += 1
                        i1 -= 1
                        j1 -= 1
                    i2 = i + 1
                    j2 = j + 1
                    while i2 <= 5 and j2 <= 5 and data[i2][j2] == data[i][j]:
                        symbols += 1
                        i2 += 1
                        j2 += 1
                    if symbols >= 3:
                        if i1 >= 0 and j1 >=0 and self.verify_move(i1,j1,ret_symbol):
                            return i1, j1, ret_symbol
                        if i2<=5 and j2<=5 and self.verify_move(i2,j2, ret_symbol):
                            return i2, j2, ret_symbol

                    symbols = 1
                    i1 = i - 1
                    j1 = j + 1
                    while i1 >= 0 and j1 <= 5 and data[i1][j1] == data[i][j]:
                        symbols += 1
                        i1 -= 1
                        j1 += 1
                    i2 = i + 1
                    j2 = j - 1
                    while i2 <= 5 and j2 >= 0 and data[i2][j2] == data[i][j]:
                        symbols += 1
                        i2 += 1
                        j2 -= 1
                    if symbols >= 3:
                        if i1>=0 and j1<=5 and self.verify_move(i1,j1, ret_symbol):
                            return i1,j1, ret_symbol
                        if i2<=5 and j2>=0 and self.verify_move(i2,j2,ret_symbol):
                            return i1,j2,ret_symbol
        return False, False, False

    def computer_move(self, row, column, symbol):
        row_m, column_m, symbol_m = self.check_win_possibility()
        #print(row_m, column_m, symbol_m)
        if symbol_m:
            self.move_order(row_m, column_m, symbol_m)
            return
        else:
            if symbol == '0':
                symbol_m = 'X'
            else:
                symbol_m = '0'
            if row-1 >= 0 and column-1>=0 and self.verify_move(row-1, column-1, symbol):
                self.move_order(row-1, column-1, symbol_m)
                return
            if row+1<=5 and column+1<=5 and self.verify_move(row+1, column+1, symbol):
                self.move_order(row+1, column+1, symbol_m)
                return
            if row - 1 >= 0 and column + 1 <= 5 and self.verify_move(row-1, column+1, symbol):
                self.move_order(row-1, column+1, symbol_m)
                return
            if row+1<=5 and column-1>=0 and self.verify_move(row+1, column-1, symbol):
                self.move_order(row+1, column-1, symbol_m)
                return
            self.random_move()

    def random_move(self):
        data = self._repo.return_data()
        for i in range(0, 6):
            for j in range(0, 6):
                if data[i][j] == ' ':
                    self.move_order(i, j, '0')
                    ok = self.check_win_status_order()
                    if ok:
                        #self._repo.remove_move(i, j)
                        self.move_order(i, j, 'X')
                    return


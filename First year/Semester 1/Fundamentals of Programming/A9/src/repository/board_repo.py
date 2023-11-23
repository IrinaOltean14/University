from src.domain.errors import RepoError
import copy

class RepoBoards:
    def __init__(self, rows = 10, columns = 10):
        self._rows = rows
        self._columns = columns
        self._emptySpace = ' '
        self._player_board = self.create_board()
        self._computer_board = self.create_board()
        self._computer_planes = []
        self._player_planes = []

    def create_board(self):
        return [[self._emptySpace for _ in range(0, self._columns)] for _ in range(0, self._rows)]

    def get_player_board(self):
        return self._player_board

    def get_computer_board(self):
        return self._computer_board

    def place_planes_repo(self,who_moves, row, column, direction):
        if who_moves == 'player':
            new_board = self._player_board
            self._player_planes.append((row,column, direction))
        else:
            new_board = self._computer_board
            self._computer_planes.append((row,column,direction))
        if direction == 'up':
            row_copy = row
            for counter in range(0, 3):
                if new_board[row_copy][column] != ' ':
                    raise RepoError('Planes are intersecting')
                row_copy += 1
            column_copy = column - 2
            for counter in range(0, 5):
                if new_board[row + 1][column_copy] != ' ' and column_copy != column:
                    raise RepoError('Planes are intersecting')
                column_copy += 1
            column_copy = column - 1
            for counter in range(0, 3):
                if new_board[row + 3][column_copy] != ' ':
                    raise RepoError('Planes are intersecting')
                column_copy += 1
            row_copy = row
            for counter in range(0, 3):
                new_board[row_copy][column] = 'X'
                row_copy += 1
            column_copy = column - 2
            for counter in range(0, 5):
                new_board[row + 1][column_copy] = 'X'
                column_copy += 1
            column_copy = column - 1
            for counter in range(0,3):
                new_board[row + 3][column_copy] = 'X'
                column_copy += 1
        if direction == 'down':
            row_copy = row
            for counter in range(0, 3):
                if new_board[row_copy][column] != ' ':
                    raise RepoError('Planes are intersecting')
                row_copy -= 1
            column_copy = column - 2
            for counter in range(0, 5):
                if new_board[row - 1][column_copy] != ' ' and column_copy != column:
                    raise RepoError('Planes are intersecting')
                column_copy += 1
            column_copy = column - 1
            for counter in range(0, 3):
                if new_board[row - 3][column_copy] != ' ':
                    raise RepoError('Planes are intersecting')
                column_copy += 1
            row_copy = row
            for counter in range(0, 3):
                new_board[row_copy][column] = 'X'
                row_copy -= 1
            column_copy = column - 2
            for counter in range(0, 5):
                new_board[row - 1][column_copy] = 'X'
                column_copy += 1
            column_copy = column - 1
            for counter in range(0, 3):
                new_board[row - 3][column_copy] = 'X'
                column_copy += 1
        if direction == 'left':
            column_copy = column
            for counter in range(0, 3):
                if new_board[row][column_copy] != ' ':
                    raise RepoError('Planes are intersecting')
                column_copy += 1
            row_copy = row - 1
            for counter in range(0, 3):
                if new_board[row_copy][column + 3] != ' ':
                    raise RepoError('Planes are intersecting')
                row_copy += 1
            row_copy = row - 2
            for counter in range(0, 5):
                if new_board[row_copy][column + 1] != ' ' and row_copy != row:
                    raise RepoError('Planes are intersecting')
                row_copy += 1
            column_copy = column
            for counter in range(0,3):
                new_board[row][column_copy] = 'X'
                column_copy += 1
            row_copy = row - 1
            for counter in range(0,3):
                new_board[row_copy][column + 3] = 'X'
                row_copy += 1
            row_copy = row - 2
            for counter in range(0,5):
                new_board[row_copy][column + 1] = 'X'
                row_copy += 1
        if direction == 'right':
            column_copy = column
            for counter in range(0, 3):
                if new_board[row][column_copy] != ' ':
                    raise RepoError('Planes are intersecting')
                column_copy -= 1
            row_copy = row - 1
            for counter in range(0,3):
                if new_board[row_copy][column - 3] != ' ':
                    raise RepoError('Planes are intersecting')
                row_copy += 1
            row_copy = row - 2
            for counter in range(0, 5):
                if new_board[row_copy][column - 1] != ' ' and row_copy != row:
                    raise RepoError('Planes are intersecting')
                row_copy += 1
            column_copy = column
            for counter in range(0, 3):
                new_board[row][column_copy] = 'X'
                column_copy -= 1
            row_copy = row - 1
            for counter in range(0, 3):
                new_board[row_copy][column - 3] = 'X'
                row_copy += 1
            row_copy = row - 2
            for counter in range(0, 5):
                new_board[row_copy][column - 1] = 'X'
                row_copy += 1
        new_board[row][column] = '$'


    def delete_plane(self, who_plays,row, column):
        if who_plays == 'player':
            plane_list = copy.deepcopy(self._computer_planes)
            board = self._computer_board
        else:
            plane_list = copy.deepcopy(self._player_planes)
            board = self._player_board
        for plane in plane_list:
            if plane[0] == row and plane[1] == column:
                direction = plane[2]
                plane_list.remove(plane)
        if who_plays == 'player':
            self._computer_planes = copy.deepcopy(plane_list)
        else:
            self._player_planes = copy.deepcopy(plane_list)
        if direction == 'up':
            row_copy = row
            for counter in range(0, 3):
                board[row_copy][column] = '0'
                row_copy += 1
            column_copy = column - 2
            for counter in range(0, 5):
                board[row + 1][column_copy] = '0'
                column_copy += 1
            column_copy = column - 1
            for counter in range(0, 3):
                board[row + 3][column_copy] = '0'
                column_copy += 1
        elif direction == 'down':
            row_copy = row
            for counter in range(0, 3):
                board[row_copy][column] = '0'
                row_copy -= 1
            column_copy = column - 2
            for counter in range(0, 5):
                board[row - 1][column_copy] = '0'
                column_copy += 1
            column_copy = column - 1
            for counter in range(0, 3):
                board[row - 3][column_copy] = '0'
                column_copy += 1
        elif direction == 'left':
            column_copy = column
            for counter in range(0, 3):
                board[row][column_copy] = '0'
                column_copy += 1
            row_copy = row - 1
            for counter in range(0, 3):
                board[row_copy][column + 3] = '0'
                row_copy += 1
            row_copy = row - 2
            for counter in range(0, 5):
                board[row_copy][column + 1] = '0'
                row_copy += 1
        elif direction == 'right':
            column_copy = column
            for counter in range(0, 3):
                board[row][column_copy] = '0'
                column_copy -= 1
            row_copy = row - 1
            for counter in range(0, 3):
                board[row_copy][column - 3] = '0'
                row_copy += 1
            row_copy = row - 2
            for counter in range(0, 5):
                board[row_copy][column - 1] = '0'
                row_copy += 1

    def move_repo(self, who_plays, row, column):
        if who_plays == 'player':
            board = self._computer_board
        else:
            board = self._player_board
        if board[row][column] == '$':
            self.delete_plane(who_plays, row, column)
            return 'YOU HIT THE CABIN! THE PLANE IS DOWN'
        if board[row][column] == 'X':
            board[row][column] = '0'
            return 'YOU HIT A PART OF A PLANE!'
        if board[row][column] == ' ':
            return 'YOU MISSED'

    def check_winner_status_repo(self, who_moves):
        if who_moves == 'player':
            board = self._computer_board
        else:
            board = self._player_board
        for row in board:
            for symbol in row:
                if symbol == 'X' or symbol == '$':
                    return 'No winner'
        if who_moves == 'player':
            return 'CONGRATULATIONS! YOU WON!'
        else:
            return 'THE COMPUTER WON'

    def get_planes(self, who_moves):
        if who_moves == 'player':
            return self._player_planes
        else:
            return self._computer_planes



import random
from src.domain.errors import ServiceError


class ComputerStrategy:
    def __init__(self, move_service):
        self._service = move_service
        self._random_moves = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
                       'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
                       'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                       'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
                       'E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
                       'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
                       'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
                       'H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
                       'I0', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9',
                       'J0', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9']
        self._moves_that_hit = []
        self._next_moves = []

    def place_planes(self):
        plane_heads = ['A0', 'A1', 'A2', 'A8', 'A9',
                       'B0', 'B1', 'B2', 'B8', 'B9',
                       'C0', 'C1', 'C2', 'C8', 'C9',
                       'H0', 'H1', 'H2', 'H8', 'H9',
                       'I0', 'I1', 'I2',  'I8', 'I9',
                       'J0', 'J1', 'J2',  'J8', 'J9']
        directions = ['up','down','left','right']
        plane_counter = 0
        while plane_counter < 3:
            plane_head = random.choice(plane_heads)
            plane_heads.remove(plane_head)
            for index in range(0,4):
                direction = directions[index]
                try:
                    self._service.place_planes_service('computer', plane_head, direction)
                    plane_counter += 1
                    break
                except ServiceError as error:
                    pass


    def compute_next_four_moves(self, move):
        if move[1] > '0':
            next_move = move[0] + chr(ord(move[1])-1)
            if next_move in self._random_moves:
                self._next_moves.append(next_move)
        if move[1] < '9':
            next_move = move[0] + chr(ord(move[1])+1)
            if next_move in self._random_moves:
                self._next_moves.append(next_move)
        if move[0] > 'A':
            next_move = chr(ord(move[0])-1) + move[1]
            if next_move in self._random_moves:
                self._next_moves.append(next_move)
        if move[0] < 'J':
            next_move = chr(ord(move[0])+1) + move[1]
            if next_move in self._random_moves:
                self._next_moves.append(next_move)

    def computer_strategy_service(self):
        #print(self._moves_that_hit)
        #print(self._next_moves)
        #print(len(self._next_moves))
        if len(self._next_moves) != 0:
            move = self._next_moves.pop()
            self._random_moves.remove(move)
            message = self._service.move_service('computer', move)
            if message == 'YOU HIT A PART OF A PLANE!':
                self.compute_next_four_moves(move)
            elif message == 'YOU HIT THE CABIN! THE PLANE IS DOWN':
                self._next_moves = []
        elif len(self._next_moves) == 0:
            move = random.choice(self._random_moves)
            self._random_moves.remove(move)
            message = self._service.move_service('computer', move)
            if message == 'YOU HIT A PART OF A PLANE!':
                self.compute_next_four_moves(move)
            elif message == 'YOU HIT THE CABIN! THE PLANE IS DOWN':
                self._next_moves = []
        return move
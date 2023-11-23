from src.repository.board_repo import RepoBoards
from src.domain.errors import ServiceError
from prettytable import PrettyTable, ALL

class UI:
    def __init__(self, move_service, computer_service):
        self._move_service = move_service
        self._computer_service = computer_service

    def print_welcome(self):
        print('Welcome to planes!')
        print('How to play:')
        print("Try to guess the opponents plane's position")
        print("If you hit the head of the computer's plane, the hole plane will be destroyed and covered by '0'")
        print("If you hit the plane's body the there will be a '0' placed only on that position")
        print("The game will let you know what you hit")
        print("The game will end when one player's planes are completely destroyed")
        self._computer_service.place_planes()
        #board = self._move_service.get_computer_board_service()
        #for row in board:
           # print(row)
        self.place_planes_player()
        self.game_manager()

    def print_board(self, board):
        table = PrettyTable()
        table.field_names = ['Indexes', ' 0 ', ' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ' ,' 9 ']
        letter = 'A'
        for row in board:
            table.add_row([letter, row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]])
            #table.add_row(['-','-','-','-','-','-','-','-','-','-','-'])
            letter = chr(ord(letter)+1)
        table.hrules = ALL
        print(table)

    def game_manager(self):
        move_list = []
        while True:
            print('IT IS YOUR TURN')
            move = input('Where do you want to strike? Enter your move: ')
            if move in move_list:
                print('You already struck there! Try another move')
            elif len(move) != 2:
                print('Please enter a valid move!')
            else:
                try:
                    message = self._move_service.move_service('player',move)
                    print(message)
                    #board = self._move_service.get_computer_board_service()
                    #for row in board:
                      #  print(row)
                except ServiceError as error:
                    print('ERROR:' + str(error))
                message = self._move_service.check_winner_status_service('player')
                if message != 'No winner':
                    print(message)
                    break
                move_list.append(move)
                print("IT IS THE COMPUTER'S TURN")
                computer_move = self._computer_service.computer_strategy_service()
                print('THE COMPUTER CHOSE TO ATTACK ' + computer_move)
                board = self._move_service.get_player_board_service()
                self.print_board(board)
                message = self._move_service.check_winner_status_service('computer')
                if message != 'No winner':
                    print(message)
                    break

    def place_planes_player(self):
        board = self._move_service.get_player_board_service()
        self.print_board(board)
        print('PLACE YOUR PLANES')
        print("Enter a valid location of a plane's head (row represented by a letter between A-J and column represented"
              " by a digit between 0-9)")

        planes_counter = 0
        while planes_counter < 3:
            planes_counter += 1
            while True:
                plane_head = input("Enter the location of the plane's head: ")
                plane_direction = input("Enter the plane's direction (up, down, right or left): ")
                try:
                    self._move_service.place_planes_service('player', plane_head, plane_direction)
                    board = self._move_service.get_player_board_service()
                    self.print_board(board)
                    break
                except ServiceError as error:
                    print('ERROR: ' + str(error))


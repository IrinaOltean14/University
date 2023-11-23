class UI:
    def __init__(self, service):
        self._service = service

    def start_game(self):
        self.display_board()

    def display_board(self):
        board = self._service.display_board()
        print(str(board))
        while True:
            print('It is your turn, you are order')
            row = input('Please enter a valid row: ')
            column = input('Please enter a valid column: ')
            symbol = input('Please enter a valid symbol (0 or X): ')
            ok = self._service.verify_move(row, column, symbol)
            if not ok:
                print('Invalid move')
            else:
                row = int(row)
                column = int(column)
                self._service.move_order(row, column, symbol)
                board = self._service.display_board()
                print(str(board))
                win = self._service.check_win_status_chaos()
                if win:
                    print('GAME OVER')
                    print('Chaos won')
                    break
                win = self._service.check_win_status_order()
                if win:
                    print('YOU WON')
                    break
                self._service.computer_move(row, column, symbol)
                board = self._service.display_board()
                print(str(board))

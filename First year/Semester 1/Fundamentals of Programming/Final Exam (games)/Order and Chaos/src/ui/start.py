from src.repo.repo import Board
from src.service.service import Service
from src.ui.ui import UI


def start():
    board = Board()
    service = Service(board)
    ui = UI(service)
    ui.start_game()

start()
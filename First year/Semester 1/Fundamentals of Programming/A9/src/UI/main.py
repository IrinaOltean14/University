from src.repository.board_repo import RepoBoards
from src.service.move_service import MoveService
from src.service.computer_move_service import ComputerStrategy
from src.UI.ui import UI


def start():
    repo = RepoBoards()
    move_service = MoveService(repo)
    computer_strategy = ComputerStrategy(move_service)
    ui = UI(move_service, computer_strategy)
    ui.print_welcome()

start()

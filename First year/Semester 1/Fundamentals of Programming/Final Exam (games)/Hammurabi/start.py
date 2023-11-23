from src.controller import Controller
from src.repo import Repo
from src.ui import UI
from src.validator import Validator


def start():
    repo = Repo()
    validator = Validator()
    controller = Controller(repo, validator)
    ui = UI(controller)
    ui.run_the_game_for_every_year()

start()

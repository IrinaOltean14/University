from src.repository import TextFileRepo
from src.services import Service, ValidationError, AsValidator

class UI:
    def __init__(self, service):
        self._service = service

    def print_menu(self):
        print('The assignments from the file are:')
        self.display_assign()

        while True:
            print('Add an assignment')
            print('Display all')
            print('Dishonesty check')
            option= input('>')
            if option == 'add':
                self.add_assign()
            if option == 'display':
                self.display_assign()
            if option == 'dishonesty check':
                self.dishonesty_check()
            if option == 'end':
                break

    def dishonesty_check(self):
        dishonesty_list = self._service.dishonesty_check()
        for dishonest in dishonesty_list:
            print(dishonest)
    def display_assign(self):
        assign = self._service.display_assign()
        for asignm in assign:
            print(asignm)

    def add_assign(self):
        assign = input('Enter assignment: ')
        parts = assign.split(',')
        id = parts[0].strip()
        name = parts[1].strip()
        solution = parts[2].strip()
        try:
            self._service.add_assign(id, name, solution)
            print('Assignment added successfully')
        except ValidationError as error:
            print('ERROR: ' + str(error))


def start():
    repo = TextFileRepo()
    validator = AsValidator()
    service = Service(repo, validator)
    ui = UI(service)
    ui.print_menu()

start()
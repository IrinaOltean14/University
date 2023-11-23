from src.errors.errorspy import *


class UI:
    def __init__(self, service):
        self._service = service

    @staticmethod
    def print_menu():
        print("Choose your option")
        print("1. Add an expense")
        print("2. Display the list of expenses")
        print("3. Filter the list so that the list contains expenses over a certain value")
        print("4. Undo")
        print("5. End the program")

    def generate_expenses(self):
        self._service.add_expense_service(5, 250, 'Rent')
        self._service.add_expense_service(10, 300, 'Groceries')
        self._service.add_expense_service(25, 150, 'Jacket')
        self._service.add_expense_service(7, 200, 'Shoes')
        self._service.add_expense_service(14, 100, 'Birthday Gift')

    def add_expense_ui(self):
        day = int(input("Enter a day: "))
        amount = int(input("Enter an amount: "))
        type_expense = input("Enter the type of the expense: ")
        self._service.add_expense_service(day, amount, type_expense)
        print("Expense added with success!")

    def filter_expenses_ui(self):
        value = int(input("Enter the value: "))
        self._service.filter_expenses_service(value)

    def print_expenses_ui(self):
        expenses = self._service.get_all_expenses_service()
        if len(expenses) == 0:
            print("No expenses!")
            return
        #print(expenses)
        for expense in expenses:
            print(expense)

    def undo_expenses_ui(self):
        expenses = self._service.get_all_expenses_service_undo()
        if len(expenses) == 0:
            print("No expenses!")
            return
        for expense in expenses:
            print(expense)

    def run(self):
        while True:
            self.print_menu()
            command = input("Enter your option: ")
            add_an_expense = '1'
            display_expenses = '2'
            filter_list_of_expenses = '3'
            undo = '4'
            end_program = '5'
            try:
                if command == add_an_expense:
                    self.add_expense_ui()
                elif command == display_expenses:
                    self.print_expenses_ui()
                elif command == filter_list_of_expenses:
                    self.filter_expenses_ui()
                elif command == undo:
                    self.undo_expenses_ui()
                elif command == end_program:
                    break
                else:
                    print('Invalid command')
            except ValueError:
                print("Error in UI")
            except ValidError as ve:
                print("ValidError: ", ve)
            except RepoError as re:
                print("Repo Error: ", re)
from src.services.service import *
from src.ui.ui import *
from src.repo.repo_in_memory import *
from src.repo.repo_text_file import *
from src.repo.repo_binary_file import *
from src.test.tests import Test
from src.errors.expensevalidation import *


def main():
    test = Test()
    test.run_all()
    validation_expense = ExpenseValidation()
    print("Choose the type of repository:")
    print("1. Memory")
    print("2. Text file")
    print("3. Binary file")
    option = input("Enter your option: ")
    memory = '1'
    text_file = '2'
    binary_file = '3'
    if option == memory:
        repo = RepoMemory()
    elif option == text_file:
        repo = RepoTextFile()
    elif option == binary_file:
        repo = RepoBinaryFile()
    else:
        print("Invalid command")
    service = Service(validation_expense, repo)
    ui = UI(service)
    ui.generate_expenses()
    ui.run()


main()

from src.domain.expenses import Expenses
from copy import deepcopy

class Service:
    def __init__(self, validation_expense, repo):
        self._validation_expense = validation_expense
        self._repo = repo

    def add_expense_service(self, day, amount, type_expense):
        expense = Expenses(day, amount, type_expense)
        self._validation_expense.validate(expense)
        self._repo.add_expense_repo(expense)


    def filter_expenses_service(self, value):
        self._repo.remove_expense_repo(value)


    def get_all_expenses_service(self):
        return self._repo.get_all_expenses_repo()

    def get_all_expenses_service_undo(self):
        return self._repo.get_all_expenses_repo_undo()

    #def get_all_expenses_service_undo(self):
     ##  self._history.pop()
     #   new_list = deepcopy(self._history.pop())
      #  print(new_list)
       # self._history.append(new_list)
        #return self._repo.get_all_expenses_repo_undo(new_list)
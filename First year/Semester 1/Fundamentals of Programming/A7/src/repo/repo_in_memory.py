from copy import deepcopy

class RepoMemory:
    def __init__(self):
        self._expenses = []
        self._history = []

    def add_expense_repo(self, expense_to_be_added):
        self._expenses.append(expense_to_be_added)
        new_list = []
        for expense in self._expenses:
            new_list.append(expense)
        self._history.append(new_list)

    def get_all_expenses_repo(self):
        return self._expenses

    def remove_expense_repo(self, value):
        there_is_no_value_smaller = False
        while there_is_no_value_smaller == False:
            there_is_no_value_smaller = True
            for expense in self._expenses:
                if expense.get_amount() < value:
                    self._expenses.remove(expense)
                    there_is_no_value_smaller = False
        new_list = []
        for expense in self._expenses:
            new_list.append(expense)
        self._history.append(new_list)

    def get_all_expenses_repo_undo(self):
        self._history.pop()
        new_list = []
        for expense in self._history[len(self._history)-1]:
            new_list.append(expense)
        self._expenses = new_list
        return self._expenses

    #def get_all_expenses_repo_undo(self, new_list):
     ##   print(self._expenses)
    #    print(new_list)
      #  self._expenses = deepcopy(new_list)
       # return self._expenses

    def clean_memory(self):
        self._expenses = []
        return self._expenses

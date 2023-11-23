from src.domain.expenses import Expenses
from src.repo.repo_in_memory import RepoMemory
from src.errors.errorspy import *


class RepoTextFile(RepoMemory):
    def __init__(self, file_path=str('expenses.txt')):
        super().__init__()
        self._file_path = file_path
        self.clean_memory()
        self._write_data_to_file()
        self._read_data_from_file()

    def _read_data_from_file(self):
        self._expenses = self.clean_memory()
        with open(self._file_path, "rt") as file:
            lines = file.readlines()
            file.close()
            for line in lines:
                if line != "":
                    line = line.strip()
                    parts = line.split(",")
                    type_expense = parts[0].strip()
                    day = int(parts[1].strip())
                    amount = int(parts[2].strip())
                    expense = Expenses(day, amount, type_expense)
                    self._expenses.append(expense)

    def _write_data_to_file(self):
        with open(self._file_path, "wt") as file:
            for expense in self.get_all_expenses_repo():
                file.write(str(expense) + "\n")
            file.close()

    def add_expense_repo(self, expense_to_be_added):
        self._read_data_from_file()
        super().add_expense_repo(expense_to_be_added)
        self._write_data_to_file()
        #return expense

    def remove_expense_repo(self, value):
        self._read_data_from_file()
        expense = super().remove_expense_repo(value)
        self._write_data_to_file()
        #return expense

    def get_all_expenses_repo(self):
        return super().get_all_expenses_repo()

    def get_all_expenses_repo_undo(self):
        expense = super().get_all_expenses_repo_undo()
        self._write_data_to_file()
        return expense


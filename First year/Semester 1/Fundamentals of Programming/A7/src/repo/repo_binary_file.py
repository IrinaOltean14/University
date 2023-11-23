import pickle
from src.repo.repo_in_memory import RepoMemory


class RepoBinaryFile(RepoMemory):
    def __init__(self, file_path=str('expenses1.bin')):
        self._file_path = file_path
        super().__init__()
        self._write_data_to_file()
        self._read_data_from_file()

    def _write_data_to_file(self):
        with open(self._file_path, "wb") as file:
            pickle.dump(super().get_all_expenses_repo(), file)
        file.close()

    def _read_data_from_file(self):
        with open(self._file_path, "rb") as file:
            expenses_list = pickle.load(file)
            file.close()
        for expense in expenses_list:
            super().add_expense_repo(expense)

    def add_expense_repo(self, expense_to_be_added):
        expense = super().add_expense_repo(expense_to_be_added)
        self._write_data_to_file()
        return expense

    def remove_expense_repo(self, value):
        expense = super().remove_expense_repo(value)
        self._write_data_to_file()
        return expense

    def get_all_expenses_repo_undo(self):
        expense = super().get_all_expenses_repo_undo()
        self._write_data_to_file()
        return expense

    def get_all_expenses_repo(self):
        return super().get_all_expenses_repo()

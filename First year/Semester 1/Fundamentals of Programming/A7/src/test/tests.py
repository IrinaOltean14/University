from src.errors.errorspy import *
from src.repo.repo_in_memory import RepoMemory
from src.services.service import Service
from src.errors.expensevalidation import ExpenseValidation


class Test:
    def run_all(self):
        self.test_add()

    def test_add(self):
        validation_expense = ExpenseValidation()
        repo = RepoMemory()
        service = Service(validation_expense, repo)
        try:
            day = 100
            amount = 123
            type_expense = 'Backpack'
            service.add_expense_service(day,amount,type_expense)
            assert False
        except ValidError as ve:
            assert str(ve) == "Invalid day (must be between 0 and 30)"

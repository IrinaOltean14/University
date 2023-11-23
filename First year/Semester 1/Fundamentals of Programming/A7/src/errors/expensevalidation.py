from src.errors.errorspy import ValidError


class ExpenseValidation:
    def __init__(self):
        pass

    @staticmethod
    def validate(expense):
        errors = ""
        if expense.get_day() < 0 or expense.get_day() > 30:
            errors += "Invalid day (must be between 0 and 30)"
        if expense.get_amount() != int(expense.get_amount()):
            errors += "The amount is not an integer"
        if len(errors) > 0:
            raise ValidError(errors)

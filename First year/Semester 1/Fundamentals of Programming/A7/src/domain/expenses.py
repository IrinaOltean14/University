class Expenses:
    def __init__(self, day, amount, type_expense):
        self._day = day
        self._amount = amount
        self._type_expense = type_expense

    def get_day(self):
        return self._day

    def set_day(self, day):
        self._day = day

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_type(self):
        return self._type_expense

    def set_type(self, type_expense):
        self._type_expense = type_expense

    def __str__(self):
        return f"{self._type_expense}, {self._day}, {self._amount}"

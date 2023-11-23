
class Repo:
    def __init__(self):
        self._population = 100
        self._acres = 1000
        self._grain = 3000

    def get_population(self):
        return self._population

    def get_acres(self):
        return self._acres

    def update_grain(self, grain):
        self._grain = grain

    def modify_grain(self, grain):
        self._grain += grain

    def modify_population(self, people):
        self._population += people

    def get_grain(self):
        return self._grain

    def buy_or_sell_acres(self, acres_to_buy, updated_grains):
        self._acres += acres_to_buy
        self._grain += updated_grains

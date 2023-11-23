from random import randint, choice


class Controller:
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator

    def get_population(self):
        return self._repo.get_population()

    def modify_population(self, people):
        self._repo.modify_population(people)

    def get_acres(self):
        return self._repo.get_acres()

    def get_harvest(self):
        harvest = randint(1, 6)
        return harvest

    def get_price(self):
        price = randint(15, 25)
        return price

    def calculate_grain(self, ate_by_rats):
        grain = self.get_grain()
        grain = grain - ate_by_rats
        self._repo.update_grain(grain)
        return grain

    def update_grain(self, grain):
        self._repo.update_grain(grain)

    def get_grain(self):
        return self._repo.get_grain()

    def buy_or_sell_acres(self, acres_to_buy_or_sell, price):
        try:
            acres_to_buy_or_sell = int(acres_to_buy_or_sell)
        except ValueError:
            raise ValueError('Input is not int')
        grain = self.get_grain()
        acres = self.get_acres()
        self._validator.validate_acres(acres, grain, acres_to_buy_or_sell, price)
        updated_grains = acres_to_buy_or_sell*price

        if acres_to_buy_or_sell > 0:
            self._repo.buy_or_sell_acres(acres_to_buy_or_sell, -updated_grains)
        else:
            self._repo.buy_or_sell_acres(acres_to_buy_or_sell, -updated_grains)

    def feed_the_population(self, units_to_feed_the_population):
        try:
            units_to_feed_the_population = int(units_to_feed_the_population)
        except ValueError:
            raise ValueError('Input not an int')
        if units_to_feed_the_population < 0:
            raise ValueError('Must be a positive integer')
        grain = self.get_grain()
        self._validator.validate_units_to_feed_the_population(units_to_feed_the_population, grain)
        self._repo.modify_grain(-units_to_feed_the_population)
        population = self.get_population()
        how_many_people_are_fed = units_to_feed_the_population//20
        how_many_people_starved = population - how_many_people_are_fed
        if how_many_people_starved < 0:
            how_many_people_starved = 0
        return how_many_people_starved

    def plant_acres(self, how_many_acres_to_plant):
        try:
            how_many_acres_to_plant = int(how_many_acres_to_plant)
        except ValueError:
            raise ValueError('The input is not an int')
        if how_many_acres_to_plant < 0:
            raise ValueError('Must be a positive integer')
        acres = self.get_acres()
        population = self.get_population()
        self._validator.validate_plant_acres(how_many_acres_to_plant, acres, population)

    def get_how_many_people_came_to_the_city(self, people_who_starved):
        if people_who_starved == 0:
            people_who_came_to_the_city = randint(0,10)
        else:
            people_who_came_to_the_city = 0
        return people_who_came_to_the_city

    def get_units_ate_by_rats(self):
        probability_list = [False, False, False, False, True]
        did_a_rat_infestation_occur = choice(probability_list)
        if did_a_rat_infestation_occur:
            percentage_of_grain_infested = randint(1, 10)
            grain = self.get_grain()
            units_ate_by_rats = int(percentage_of_grain_infested*grain/100)
        else:
            units_ate_by_rats = 0
        return units_ate_by_rats

from src.validator import ValidationError


class UI:
    def __init__(self, controller):
        self._controller = controller

    def print_data_for_every_year(self, year, people_who_starved, people_who_came_to_the_city,ate_by_rats, price, harvest):
        print('In year ' + str(year) + ', ' + str(people_who_starved) + ' people starved')
        print(str(people_who_came_to_the_city) + ' people came to the city')
        population = self._controller.get_population()
        print('City population is ' + str(population))
        acres = self._controller.get_acres()
        print('City owns ' + str(acres) + ' acres of land')
        print('Harvest was ' + str(harvest) + ' units per acre')
        print('Rats ate ' + str(ate_by_rats) + ' units')
        print('Land price is ' + str(price) + ' units per year')
        grain = self._controller.calculate_grain(ate_by_rats)
        print('\n')
        print('Grain stocks are ' + str(grain) + ' units')
        print('\n')

    def run_the_game_for_every_year(self):
        price = 20
        self.print_data_for_every_year(1, 0, 0, 200, 20, 3)
        how_many_people_starved, how_many_acres_to_plant = self.make_decisions(price)
        for year in range(2, 6):
            people_who_came_to_the_city = self._controller.get_how_many_people_came_to_the_city(how_many_people_starved)
            self._controller.modify_population(-how_many_people_starved)
            self._controller.modify_population(people_who_came_to_the_city)
            harvest = self._controller.get_harvest()
            self._controller.update_grain(how_many_acres_to_plant*harvest)
            grain = self._controller.get_grain()
            units_ate_by_rats = self._controller.get_units_ate_by_rats()
            price = self._controller.get_price()
            self.print_data_for_every_year(year, how_many_people_starved, people_who_came_to_the_city, units_ate_by_rats, price, harvest)
            if year != 5:
                how_many_people_starved, how_many_acres_to_plant = self.make_decisions(price)
        population = self._controller.get_population()
        acres = self._controller.get_acres()
        if acres > 1000 and population > 100:
            print('YOU WON')
        else:
            print('YOU LOST')


    def make_decisions(self, price):
        while True:
            acres_to_buy_or_sell = input('Acres to buy/sell (+/-) -> ')
            try:
                self._controller.buy_or_sell_acres(acres_to_buy_or_sell, price)
                break
            except ValueError as error:
                print('ERROR: ' + str(error))
            except ValidationError as error:
                print('ERROR: ' + str(error))
        while True:
            units_to_feed_the_population = input('Units to feed the population -> ')
            try:
                how_many_people_starved = self._controller.feed_the_population(units_to_feed_the_population)
                break
            except ValueError as error:
                print('ERROR: ' + str(error))
            except ValidationError as error:
                print('ERROR: ' + str(error))

        while True:
            how_many_acres_to_plant = input('Acres to plant -> ')
            try:
                self._controller.plant_acres(how_many_acres_to_plant)
                break
            except ValueError as error:
                print('ERROR: ' + str(error))
            except ValidationError as error:
                print('ERROR: ' + str(error))
        print('\n')

        how_many_people_starved = int(how_many_people_starved)
        how_many_acres_to_plant = int(how_many_acres_to_plant)
        return how_many_people_starved, how_many_acres_to_plant

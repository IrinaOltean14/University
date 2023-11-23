class ValidationError(Exception):
    pass

class Validator:
    def __init__(self):
        pass

    def validate_acres(self, acres, grain, acres_to_buy_or_sell, price):
        if acres_to_buy_or_sell > 0:
            if acres_to_buy_or_sell*price > grain:
                raise ValidationError('Not enough grain to buy that many acres')
        else:
            if acres_to_buy_or_sell*(-1) > acres:
                raise ValidationError('You can not sell acres that you do not have')

    def validate_units_to_feed_the_population(self,units_to_feed_the_population, grains):
        if units_to_feed_the_population > grains:
            raise ValidationError('You can not feed the population with grains that you do not have')

    def validate_plant_acres(self, how_many_acres_to_plant, acres, population):
        if how_many_acres_to_plant > acres:
            raise ValidationError('You can not plant more acres than you have')
        elif how_many_acres_to_plant//10 > population:
            raise ValidationError('Not enough people to plant that many acres')



import unittest

from src.controller import Controller
from src.repo import Repo
from src.validator import Validator, ValidationError


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = Repo()
        self._validator = Validator()
        self._controller = Controller(self._repo, self._validator)

    def tearDown(self) -> None:
        pass

    def test_buy_sell_acres(self):
        self._controller.buy_or_sell_acres(10, 20)
        self.assertEqual(self._controller.get_acres(), 1010)
        self._controller.buy_or_sell_acres(10, 20)
        self.assertEqual(self._controller.get_grain(), 2600)
        with self.assertRaises(ValidationError) as error:
            self._controller.buy_or_sell_acres(1001, 20)
        self.assertEqual(str(error.exception), 'Not enough grain to buy that many acres')
        with self.assertRaises(ValidationError) as error:
            self._controller.buy_or_sell_acres(-2001, 20)
        self.assertEqual(str(error.exception), 'You can not sell acres that you do not have')

    def test_feed_the_population(self):
        with self.assertRaises(ValidationError) as error:
            self._controller.feed_the_population(3200)
        self.assertEqual(str(error.exception), 'You can not feed the population with grains that you do not have')
        self._controller.feed_the_population(2000)
        self.assertEqual(self._controller.get_grain(), 1000)

    def test_plant_acres(self):
        with self.assertRaises(ValidationError) as error:
            self._controller.plant_acres(1500)
        self.assertEqual(str(error.exception), 'You can not plant more acres than you have')

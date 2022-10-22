from calculator import Calculator
from unittest import TestCase


class TestCalculator(TestCase):

    def setUp(self):
        self.vypocet = Calculator()

    def test_scitani(self):

        self.assertEqual(self.vypocet.scitani(2, 2), 4)

    def test_odcitani(self):

        self.assertEqual(self.vypocet.odcitani(8, 4), 4)

    def test_nasobeni(self):

        self.assertEqual(self.vypocet.nasobeni(2, 4), 8)

    def test_deleni(self):

        self.assertEqual(self.vypocet.deleni(9, 3), 3)
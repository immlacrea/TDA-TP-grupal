import unittest
from Ejercicio_1 import extract_coins_data_from_file, play_the_game

winner_sophia = "Sophia"

class TESTEjercicio1(unittest.TestCase):


    def test_20_elements(self):
        data = "20.txt"
        coins = extract_coins_data_from_file(data)
        winner = play_the_game(coins)
        self.assertEqual(winner, winner_sophia)

    def test_25_elements(self):
        data = "25.txt"
        coins = extract_coins_data_from_file(data)
        winner = play_the_game(coins)
        self.assertEqual(winner, winner_sophia)

    def test_50_elements(self):
        data = "50.txt"
        coins = extract_coins_data_from_file(data)
        winner = play_the_game(coins)
        self.assertEqual(winner, winner_sophia)

    def test_100_elements(self):
        data = "100.txt"
        coins = extract_coins_data_from_file(data)
        winner = play_the_game(coins)
        self.assertEqual(winner, winner_sophia)

    def test_1mil_elements(self):
        data = "1000.txt"
        coins = extract_coins_data_from_file(data)
        winner = play_the_game(coins)
        self.assertEqual(winner, winner_sophia)

    def test_20mil_elements(self):
        data = "20000.txt"
        coins = extract_coins_data_from_file(data)
        winner = play_the_game(coins)
        self.assertEqual(winner, winner_sophia)

    def test_10mil_elements(self):
        data = "10000.txt"
        coins = extract_coins_data_from_file(data)
        winner = play_the_game(coins)
        self.assertEqual(winner, winner_sophia)
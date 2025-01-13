import unittest
from sophia_greedy import extract_coins_data_from_file, greedy_strategy

winner_sophia = "Sophia"

class TESTEjercicio1(unittest.TestCase):


    def test_20_elements(self):
        data = "20.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )

    def test_25_elements(self):
        data = "25.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )

    def test_50_elements(self):
        data = "50.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )

    def test_100_elements(self):
        data = "100.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )

    def test_1mil_elements(self):
        data = "1000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )

    def test_20mil_elements(self):
        data = "20000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )

    def test_10mil_elements(self):
        data = "10000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )
        
    def test_15mil_elements(self):
        data = "15000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )
    
    def test_16mil_elements(self):
        data = "16000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )
        
    def test_17mil_elements(self):
        data = "17000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )
    
    def test_18mil_elements(self):
        data = "18000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )
    
    def test_19mil_elements(self):
        data = "19000.txt"
        coins = extract_coins_data_from_file(data)
        sophia_coins, mateo_coins = greedy_strategy(coins)
        self.assertTrue(sum(num for num, _ in sophia_coins) > sum(num for num, _ in mateo_coins) )

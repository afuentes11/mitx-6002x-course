from random import seed
from .knapsack import *

ITEMS_QTY = 10
MAX_CALORIES = 1000
SEED = 20398567

def test_greedy_and_dp_algorithms():
    
    seed(SEED)

    menu = built_menu(items_qty=ITEMS_QTY)
    menu.summary()
    
    test_greedy_algorithm(menu, max_calories=MAX_CALORIES)
    dp_knapsack(menu, max_calories=MAX_CALORIES).summary()
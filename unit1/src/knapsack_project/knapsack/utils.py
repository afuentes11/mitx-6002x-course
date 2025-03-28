from random import randint, seed
from .models import *
from .greedy import *

def built_menu(items_qty, minmax_calories=(1, 500), minmax_tastiness=(1, 100)):
    return Menu([Food(
        name=str(i),
        calories=randint(*minmax_calories),
        tastiness=randint(*minmax_tastiness)
    ) for i in range(1, items_qty + 1)])


def test_greedy_algorithm(menu, max_calories):

    metrics = [
        ("calories", lambda f: 1/f.get_calories()),
        ("tastiness", Food.get_tastiness),
        ("ratio", Food.get_ratio),
    ]

    for name, metric in metrics:
        print(f"Selected by {name}")
        menu_result = greedy_knapsack(menu, metric, max_calories)
        menu_result.summary()
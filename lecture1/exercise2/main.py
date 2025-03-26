from ..utils.object import Object
from ..utils.utils import build_objects, test_metrics
from ..utils.greedy_knapsack import greedy_knapsack

NAMES = ["Clock", "Picture", "Radio", "Vase", "Book", "Computer"]
VALUES = [175, 90, 20, 50, 10, 200]
WEIGHTS = [10, 9, 4, 2, 1, 20]

MAX_WEIGHT = 20

class Item(Object):
    def __init__(self, name: str, weight: int, value: int):
        super().__init__(name, weight, value)

    def get_ratio(self):
        return self.value / self.weight


def main():
    
    items = build_objects(Item, NAMES, WEIGHTS, VALUES)

    metrics =[ 
        ("max value", lambda item: item.get_value()),
        ("min weight", lambda item: 1/item.get_weight()),
        ("max ratio", lambda item: item.get_ratio())
    ]

    test_metrics(items, MAX_WEIGHT, metrics, greedy_knapsack)


if __name__ == "__main__":
    main()
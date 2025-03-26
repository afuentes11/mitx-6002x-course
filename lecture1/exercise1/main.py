from ..utils import *

NAMES = ["Dirt", "Computer", "Fork", "Problem set"]
WEIGHTS = [4, 10, 5, 0]
VALUES = [0, 30, 1, -10]

MAX_WEIGHT = 14

class Home_Object(Object):
    def __init__(self, name: str, weight: int, value: int):
        super().__init__(name, weight, value)

    def metric1(self) -> float:
        return self.value / self.weight

    def metric2(self) -> float:
        return -self.weight

    def metric3(self) -> float:
        return self.value


def main():
    
    objects = build_objects(Home_Object, NAMES, WEIGHTS, VALUES)

    metricts = [
        ("metric1", lambda obj: obj.metric1()),
        ("metric2", lambda obj: obj.metric2()),
        ("metric3", lambda obj: obj.metric3()),
    ]

    test_metrics(objects, MAX_WEIGHT, metricts, greedy_knapsack)


if __name__ == "__main__":
    main()

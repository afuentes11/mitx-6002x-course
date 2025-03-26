from .object import Object
from typing import List, Type, Any

def build_objects(
    object_type: Type[Object], names: List[str], weights: List[int], values: List[int]
) -> List[Object]:
    """
    Builds a list of objects of a specified type.

    Args:
        names: List of object names.
        weights: List of object weights.
        values: List of object values.
        object_type: The class type of the objects to create, defaults to Object
    """
    return [object_type(names[i], weights[i], values[i]) for i in range(len(names))]


def test_metrics(objects, max_weight, metricts, algorithm):
    """
    Test different metrics with a given algorithm.

    This function iterates through a list of metrics and applies a given
    algorithm to a set of objects with each metric. It then prints the
    results, including the maximum value obtained and the objects selected.

    Args:
        objects (List[Object]): A list of objects to be considered.
        max_weight (int): The maximum weight allowed.
        metricts (List[Tuple[str, Callable]]): A list of tuples, where each
            tuple contains a metric name (str) and the metric function
            (Callable).
        algorithm (Callable): The algorithm to be applied. This should be a
            function that takes (objects, max_weight, metric) as arguments.
    """

    for metric_name, metric in metricts:
        try:
            max_value, objects_selected = algorithm(objects, max_weight, metric)
            print(f"{metric_name}: {max_value}")
            for obj in objects_selected:
                print(f"{obj}")
        except Exception as e:
            print(f"{metric_name}: Error {e}")
        print()
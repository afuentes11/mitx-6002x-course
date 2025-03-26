def greedy_knapsack(objects, max_weight, metric):
    """
    Apply a greedy algorithm to maximize the value of objects in a knapsack.

    Args:
        objects (list): A list of objects, each with a get_value() and get_weight() method.
        max_weight (int): The maximum weight the knapsack can hold.
        metric (callable): A function that takes an object and returns a value used for sorting.

    Returns:
        tuple: A tuple containing the maximum value obtained and a list of the objects selected.
    """

    copy_objects = sorted(objects, key=metric, reverse=True)

    max_value = 0
    objects_selected = []

    for obj in copy_objects:
        if max_weight >= obj.get_weight():
            max_weight -= obj.get_weight()
            max_value += obj.get_value()
            objects_selected.append(obj)

    return max_value, objects_selected
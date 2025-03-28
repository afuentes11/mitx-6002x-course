
NUMBER = 3

def look_for_things(myList):
    """
    Looks at all elements

    Big(O): n
    """
    for n in myList:
        if n == NUMBER:
            return True
    return False


def look_for_other_things(myList):
    """
    Looks at all pairs of elements

    Big(O): n^2
    """
    for n in myList:
        for m in myList:
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False


def get_all_subsets(some_list):
    """
    Returns all subsets of size 0 - len(some_list) for some_list

    Big(O): 2^n
    """
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset) # Add without first_elt
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset) # Add with first_elt

    # Each elt can to be or not to be in the subset, in another words, it's scan to be 0 or 1. 
    return subsets


def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False


def main():
    pass


if __name__ == '__main__':
    main()
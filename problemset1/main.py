###########################
# 6.00.2x Problem Set 1: Space Cows 

from .utils import get_partitions
import time
from random import randint

#================================
# Part A: Transporting Space Cows
#================================

def generate_cows(qty):
    """
    Generates a dictionary representing cows with unique IDs and random weights.

    Parameters:
    qty (int): The number of cows to generate.

    Returns:
    dict: A dictionary where keys are string representations of cow IDs (starting from '1')
          and values are random integers representing the weight of each cow (between 1 and 10).
    """
    return {str(i):randint(1, 10) for i in range(1, qty + 1)}



def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    copy_cows = sorted(cows.items(), key=lambda cow: cow[1], reverse=True)

    trips = []
    weights = []

    for name, weight in copy_cows:

        for i in range(len(trips)):
            if (limit - weights[i]) >= weight:
                trips[i].append(name)
                weights[i] += weight
                break
        else:
            if  limit >= weight:
                trips.append([name])
                weights.append(weight)
    
    return trips
            


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    best_trips = None

    for trips in get_partitions(cows.keys()):
        
        for trip in trips:
            if sum(map(lambda x: cows[x], trip)) > limit:
                break
        else:
            if best_trips == None:
                best_trips = trips
            else:
                best_trips = trips if len(trips) <= len(best_trips) else best_trips

    return best_trips


def dynamic_cow_transport(cows, trips):
    pass 


        
# Problem 3
def compare_cow_transport_algorithms(cows, limit):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    algorithms = [
        ("Greedy Algorithm", greedy_cow_transport),
        ("Brute Force Algorithm", brute_force_cow_transport)
    ]

    for name, function in algorithms:
        start = time.time()
        result = function(cows, limit)
        end = time.time()

        print(name, f"# trips: {len(result)}", f"Time: {end - start:.10f}", sep="\n", end="\n\n")


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

def main():
    # cows = load_cows("problemset1/ps1_cow_data.txt")
    cows = generate_cows(10) 

    limit=10

    for i in range(2, 13):
        print(i-1, " - ", sum(1 for _ in get_partitions(range(1, i))))

    exit()

    #print(greedy_cow_transport(cows, limit))
    #print(brute_force_cow_transport(cows, limit))

    compare_cow_transport_algorithms(cows, limit)

if __name__ == "__main__":
    main()
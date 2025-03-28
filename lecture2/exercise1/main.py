def power_set(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """

    N = len(items)
    #memo = [] # memo for debug 
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):

            choice = i // (3**j) # Convierte el numero en una representaion de base 3

            if choice % 3 == 1:
                combo1.append(items[j])
            
            if choice % 3 == 2:
                combo2.append(items[j])

        #memo.append((combo1, combo2))
        yield combo1, combo2
    

def main():
    items = [x for x in range(1, 3)]

    ps = yieldAllCombos(items)

    for x in ps:
        print(x)

if __name__ == "__main__":
    main()

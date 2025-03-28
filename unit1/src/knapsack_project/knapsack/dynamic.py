from .models import Menu

def dp_knapsack(menu: Menu, max_calories: int, with_memo=False, memo=None):

    if memo is None:
        memo = {}
    
    key = (len(menu), max_calories)
    
    if key in memo:
        return memo[key]
    
    if len(menu) == 0 or max_calories == 0:
        return Menu()

    food = menu[0]

    if food.get_calories() > max_calories:
        result = dp_knapsack(menu[1:], max_calories, memo)
    
    else:

        menu_with_food = dp_knapsack(menu[1:], max_calories - food.get_calories(), memo)
        menu_with_food.add(food)

        menu_without_food = dp_knapsack(menu[1:], max_calories, memo)

        if menu_with_food.total_tastiness >= menu_without_food.total_tastiness:
            result = menu_with_food
        else:
            result = menu_without_food
    
    memo[key] = result
    
    return memo[key]
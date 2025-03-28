from .models import Menu
        
def greedy_knapsack(menu, metric, max_calories=600):

    copy_menu: Menu = Menu(sorted(menu, key=metric, reverse=True))

    menu_result = Menu()

    for food in copy_menu:
        if max_calories >= food.get_calories():
            menu_result.add(food)
            max_calories -= food.get_calories()
    
    return menu_result
class Food():
    def __init__(self, name, calories, tastiness):
        self.name = name
        self.calories = calories
        self.tastiness = tastiness

    def get_calories(self):
        return self.calories

    def get_tastiness(self):
        return self.tastiness
    
    def get_ratio(self):
        return self.tastiness / self.calories 

    def __repr__(self):
        return f"name: {self.name} - <calories: {self.calories}, tastiness: {self.tastiness}>"

    def __str__(self):
        return f"name: {self.name} - <calories: {self.calories}, tastiness: {self.tastiness}>"



class Menu():
    def __init__(self, foods=None):
        if foods is None: foods = []  # Se crea una nueva lista en cada instancia
        if not isinstance(foods, list):
            raise TypeError("Debe ser una lista")
        self.foods = foods
        self._update_totals()

    def _update_totals(self):
        self.total_calories = sum(food.get_calories() for food in self.foods)
        self.total_tastiness = sum(food.get_tastiness() for food in self.foods)

    def add(self, food: Food):
        self.foods.append(food)
        self._update_totals()

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Menu(self.foods[index])
        return self.foods[index]

    def __iter__(self):
        return iter(self.foods)

    def __len__(self):
        return len(self.foods)
        
    def summary(self):
        print(f"total tastiness: {self.total_tastiness}", f"total calories: {self.total_calories}", self.__str__(), sep="\n", end="\n\n")

    def __str__(self):
        return "\n".join(map(lambda food: food.__str__(), self.foods))
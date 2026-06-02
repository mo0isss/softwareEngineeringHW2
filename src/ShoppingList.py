from Ingredient import Ingredient
from Recipe import Recipe

class ShoppingList:
    def __init__(self) -> None:
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)

        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str) -> None:
        newItems = []
        for item in self._items:
            if item[1] != title:
                newItems.append(item)
        self._items = newItems
    
    def get_list(self):
        dict = {}

        for item in self._items:
            ingredient = item[0]
            key = (ingredient.name, ingredient.unit)

            if key in dict.keys():
                dict[key] += ingredient.quantity
            else:
                dict[key] = ingredient.quantity
        
        result = []

        for key in dict.keys():
            result.append(Ingredient(key[0], dict[key], key[1]))
        
        result.sort(key=lambda x: x.name)

        return result
    
    def __add__(self, other):
        result = ShoppingList()
        result._items = self._items.copy() + other._items.copy()

        return result

        
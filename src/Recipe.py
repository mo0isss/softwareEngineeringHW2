from Ingredient import Ingredient 

class Recipe:
    def __init__(self, title: str, ingredients: list) -> None:
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient) -> None:
        if ingredient in self.ingredients:
            self.ingredients[self.ingredients.index(ingredient)].quantity += ingredient.quantity
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
        newIngreditents = []
        for ingredient in self.ingredients:
            newIngredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
            newIngreditents.append(newIngredient)
        
        return Recipe(self.title, newIngreditents)
    
    def __len__(self) -> int:
        return len(self.ingredients)
    
    def __str__(self) -> str:
        s = self.title + '\n'
        counter = 1
        for ingredient in self.ingredients:
            s += f'{counter}: {ingredient}\n'
        
        return s

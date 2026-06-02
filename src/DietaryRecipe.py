from Recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients = None):
        if ingredients is None:
            ingredients = []
            
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        scaledRecipe = super().scale(ratio)
        return DietaryRecipe(scaledRecipe.title, self.diet_type, scaledRecipe.ingredients)
    
    def __str__(self) -> str:
        return f"[{self.diet_type}] {super().__str__()}"
import pytest
from src.Ingredient import Ingredient
from src.Recipe import Recipe

@pytest.fixture
def recipeOne():
    ingregient1 = Ingredient("Картошка", 500, "г")
    ingredient2 = Ingredient("Сыр", 200, "г")
    ingredient3 = Ingredient("Перец", 20, "г")
    return Recipe("Картошка с сыром", [ingregient1, ingredient2, ingredient3])

def test_createRecipe(recipeOne):
    assert recipeOne.title == "Картошка с сыром"
    assert len(recipeOne) == 3
    assert recipeOne.ingredients[0].name == "Картошка"
    assert recipeOne.ingredients[1].name == "Сыр"
    assert recipeOne.ingredients[2].name == "Перец"

def test_addNewIngredient(recipeOne):
    ingredient = Ingredient("Масло", 20, "мл")
    recipeOne.add_ingredient(ingredient)
    assert len(recipeOne) == 4
    assert recipeOne.ingredients[3].name == "Масло"

def test_addOldIngredient(recipeOne):
    ingredient = Ingredient("Сыр", 100, "г")
    recipeOne.add_ingredient(ingredient)
    assert len(recipeOne) == 3
    assert recipeOne.ingredients[1].quantity == 300

def test_scaleReturnsNewRecipe(recipeOne):
    scaledRecipe = recipeOne.scale(2)
    assert scaledRecipe is not recipeOne
    assert len(scaledRecipe.ingredients) == len(recipeOne.ingredients)
    assert scaledRecipe.title == recipeOne.title
    assert scaledRecipe.ingredients[0].quantity == 1000
    assert scaledRecipe.ingredients[1].quantity == 400
    assert scaledRecipe.ingredients[2].quantity == 40

def test_scaleRatioBelowZero(recipeOne):
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        recipeOne.scale(-3)

def test_lenReturnsLength(recipeOne):
    assert len(recipeOne) == 3
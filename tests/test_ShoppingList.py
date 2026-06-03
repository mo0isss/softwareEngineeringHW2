import pytest
from src.Ingredient import Ingredient
from src.Recipe import Recipe
from src.ShoppingList import ShoppingList

@pytest.fixture
def recipeOne():
    ingregient1 = Ingredient("Картошка", 500, "г")
    ingredient2 = Ingredient("Сыр", 200, "г")
    ingredient3 = Ingredient("Перец", 20, "г")
    return Recipe("Картошка с сыром", [ingregient1, ingredient2, ingredient3])

@pytest.fixture
def recipeTwo():
    ing1 = Ingredient("Макароны", 300, "г")
    ing2 = Ingredient("Сыр", 100, "г")
    return Recipe("Макароны с сыром", [ing1, ing2])

def test_mustAddRecipe(recipeOne):
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipeOne, 1)
    assert len(shoppingList._items) == 3

    ingredients = [item[0] for item in shoppingList._items]
    assert ingredients[0].name == "Картошка"
    assert ingredients[0].quantity == 500
    assert ingredients[1].name == "Сыр"
    assert ingredients[1].quantity == 200
    assert ingredients[2].name == "Перец"
    assert ingredients[2].quantity == 20

    recipeTitles = [item[1] for item in shoppingList._items]
    assert recipeTitles[0] == recipeOne.title
    assert recipeTitles[1] == recipeOne.title

def test_mustAddRecipeWithScale(recipeOne):
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipeOne, 2)
    assert len(shoppingList._items) == 3

    ingredients = [item[0] for item in shoppingList._items]
    assert ingredients[0].name == "Картошка"
    assert ingredients[0].quantity == 1000
    assert ingredients[1].name == "Сыр"
    assert ingredients[1].quantity == 400

    recipeTitles = [item[1] for item in shoppingList._items]
    assert recipeTitles[0] == recipeOne.title
    assert recipeTitles[1] == recipeOne.title
    
def test_portionsBelowZero(recipeOne):
    shoppingList = ShoppingList()
    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        shoppingList.add_recipe(recipeOne, -1)

def test_removeRecipe(recipeOne, recipeTwo):
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipeOne, 1)
    shoppingList.add_recipe(recipeTwo, 1)
    
    assert len(shoppingList._items) == 5

    shoppingList.remove_recipe(recipeOne.title)
    assert len(shoppingList._items) == 2
    titles = [item[1] for item in shoppingList._items]
    assert titles[0] == recipeTwo.title
    assert titles[1] == recipeTwo.title

def test_removeNonExistantRecipe(recipeOne):
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipeOne, 1)
    beforeDelete = shoppingList._items.copy()
    shoppingList.remove_recipe("Банановый пай")
    assert shoppingList._items == beforeDelete

def test_sameIngredientsSumAndSorted(recipeOne, recipeTwo):
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipeOne, 1)
    shoppingList.add_recipe(recipeTwo, 1)

    resultList = shoppingList.get_list()

    assert len(resultList) == 4

    assert resultList[0].name == "Картошка"
    assert resultList[0].quantity == 500
    assert resultList[1].name == "Макароны"
    assert resultList[1].quantity == 300
    assert resultList[2].name == "Перец"
    assert resultList[2].quantity == 20
    assert resultList[3].name == "Сыр"
    assert resultList[3].quantity == 300
    
def test_uniteTwoLists(recipeOne, recipeTwo):
    list1 = ShoppingList()
    list1.add_recipe(recipeOne, 1)
    list2 = ShoppingList()
    list2.add_recipe(recipeTwo, 2)
    unitedList = list1 + list2

    assert len(unitedList._items) == len(list1._items) + len(list2._items)

    resultList = unitedList.get_list()

    assert resultList[0].name == "Картошка"
    assert resultList[0].quantity == 500
    assert resultList[1].name == "Макароны"
    assert resultList[1].quantity == 600
    assert resultList[2].name == "Перец"
    assert resultList[2].quantity == 20
    assert resultList[3].name == "Сыр"
    assert resultList[3].quantity == 400

def test_addDoesNotTouchOriginalLists(recipeOne, recipeTwo):
    list1 = ShoppingList()
    list1.add_recipe(recipeOne, 1)
    list2 = ShoppingList()
    list2.add_recipe(recipeTwo, 1)

    list1_copy = list1._items.copy()
    list2_copy = list2._items.copy()
    unionList = list1 + list2

    assert list1._items == list1_copy
    assert list2._items == list2_copy
    
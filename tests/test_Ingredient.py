import pytest
from src.Ingredient import Ingredient

def test_createIngredient():
    ingregient = Ingredient("Кока-кола", 550.0, "мл")

    assert ingregient.name == "Кока-кола"
    assert ingregient.quantity == 550.0
    assert ingregient.unit == "мл"

def test_strReturn():
    ingregient = Ingredient("Кока-кола", 550.0, "мл")

    assert str(ingregient) == "Кока-кола: 550.0 мл"

def test_eqMustBeEqual():
    ingregient1 = Ingredient("Кока-кола", 550.0, "мл")
    ingregient2 = Ingredient("Кока-кола", 122.0, "мл")

    assert ingregient1 == ingregient2

def test_eqDifferentNames():
    ingregient1 = Ingredient("Кока-кола", 550.0, "мл")
    ingregient2 = Ingredient("Пепси", 550.0, "мл")

    assert ingregient1 != ingregient2

def test_eqDifferentUnits():
    ingregient1 = Ingredient("Кока-кола", 550.0, "мл")
    ingregient2 = Ingredient("Кока-кола", 550.0, "л")

    assert ingregient1 != ingregient2
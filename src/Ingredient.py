class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __str__(self):
        return f'{self.name}: {self.quantity} {self.unit}'
    
    def __repr__(self):
        return f'Ingredient(\'{self.name}\', {self.quantity}, \'{self.unit}\')'
    
    def __eq__(self, value):
        return self.name == value.name and self.unit == value.unit
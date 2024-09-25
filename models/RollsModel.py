class RollsModel:

    def __init__(self, name: str, ingredients: list, weight: float, quantity: int, price: float,
                 client_ingredients: list = None):
        self.__name = name
        self.__ingredients = ingredients
        self.__weight = weight
        self.__quantity = quantity
        self.__price = price
        if client_ingredients is not None:
            self.__client_ingredients = client_ingredients
        else:
            self.__client_ingredients = []

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_weight(self):
        return self.__weight

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def get_client_ingredients(self):
        return self.__client_ingredients

    def set_ingredients(self, new_ingredients: list):
        if type(new_ingredients) is list:
            self.__ingredients.clear()
            self.__ingredients.extend(new_ingredients)
        else:
            return 'Неверный ввод. Тип данных должен быть \'list\''

    def set_quantity(self, new_quantity: int):
        if type(new_quantity) is int:
            self.__quantity = new_quantity
        else:
            return 'Неверный ввод. Тип данных должен быть \'int\''

    def set_weight(self, new_weight: float):
        if type(new_weight) is float:
            self.__weight = new_weight
        else:
            return 'Неверный ввод. Тип данных должен быть \'float\''

    def set_price(self, new_price: float):
        if type(new_price) is float:
            self.__price = new_price
        else:
            return 'Неверный ввод. Тип данных должен быть \'float\''

    def add_client_ingredients(self):
        self.__ingredients.extend(self.get_client_ingredients())

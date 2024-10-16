import json
import time

class RollsModel:

    def __init__(self, name: str, ingredients: list, weight: float, quantity: int, price: float, picture,
                 client_ingredients: list = None):
        self.__name = name
        self.__ingredients = ingredients
        self.__weight = weight
        self.__quantity = quantity
        self.__price = price
        self.__picture = picture
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

    def get_picture(self):
        return self.__picture

    def get_client_ingredients(self):
        return self.__client_ingredients

    def set_ingredients(self, new_ingredients: list):
        self.__ingredients.clear()
        self.__ingredients.extend(new_ingredients)

    def set_quantity(self, new_quantity: int):
        self.__quantity = new_quantity

    def set_weight(self, new_weight: float):
        self.__weight = new_weight

    def set_price(self, new_price: float):
        self.__price = new_price

    def set_picture(self, new_picture):
        self.__picture = new_picture

    def add_client_ingredients(self):
        if self.__client_ingredients:
            self.__ingredients.extend(self.get_client_ingredients())

    def make_rolls(self):
        quantity_client_ingredients = len(self.get_client_ingredients())
        all_ingredients = self.get_ingredients()
        new_price = self.get_price()
        new_weight = self.get_weight()
        if quantity_client_ingredients:
            self.add_client_ingredients()
            all_ingredients = self.get_ingredients()
            new_price = new_price + quantity_client_ingredients * 25
            new_weight = new_weight + quantity_client_ingredients * 10

        ordered_roll = {
            'name' : self.get_name(),
            'ingredients' : all_ingredients,
            'weight' : new_weight,
            'quantity' : self.get_quantity(),
            'price' : new_price
        }
        return ordered_roll


    def save_order_to_json(self, order):
        filename = fr'orders\{round(time.time(), 2)}_{order}.json'
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.make_rolls(), fp, ensure_ascii=False, indent=2)
        return f'Заказ {order} сохранен в файл {filename}.'

    def get_data_from_json(self, filename):
        with open(fr'{filename}.json', 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data

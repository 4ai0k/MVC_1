import os
class RollsController:

    def __init__(self, model):
        self.model = model

    def restaurant_menu(self):
        roll_data = (f'Роллы : {self.model.get_name()}\n'
                     f'Вес : {self.model.get_weight()}\n'
                     f'Количество : {self.model.get_quantity()}\n'
                     f'Цена : {self.model.get_price()}\n'
                     f'Состав : {', '.join(self.model.get_ingredients())}')
        return roll_data

    def site_restaurant_menu(self):
        roll_data = (f'Роллы : {self.model.get_name()}\n'
                     f'Вес 1 штуки : {self.model.get_weight()}\n'
                     f'Количество : {self.model.get_quantity()}\n'
                     f'Цена : {self.model.get_price()}\n'
                     f'Состав : {', '.join(self.model.get_ingredients())}\n'
                     f'Фото : {os.startfile(self.model.get_picture())}')
        return roll_data

    def set_ingredients(self, user_rights, new_ingredients: list):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_ingredients(new_ingredients)
            return 'Рецепт изменен!'
        else:
            return 'forbidden'

    def set_quantity(self, user_rights, new_quantity: int):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_quantity(new_quantity)
            return 'Количество изменено!'
        else:
            return 'forbidden'

    def set_weight(self, user_rights, new_weight: int):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_weight(new_weight)
            return 'Вес изменён!'
        else:
            return 'forbidden'

    def set_price(self, user_rights, new_price: int):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_price(new_price)
            return 'Цена измененa!'
        else:
            return 'forbidden'

    def set_picture(self, user_rights, new_picture: int):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_picture(new_picture)
            return 'Фото изменено!'
        else:
            return 'forbidden'

    def save_order_to_json(self, order):
        return self.model.save_order_to_json(order)

    def get_data_from_json(self, user_rights, order):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            return self.model.get_data_from_json(order)
        else:
            return 'forbidden'
class RollsController:

    def __init__(self, model):
        self.model = model

    def restaurant_menu(self):
        roll_data = (f'Роллы : {self.model.get_name()}\n'
                     f'Вес : {self.model.get_weight()}'
                     f'Количество : {self.model.get_quantity()}\n'
                     f'Цена : {self.model.get_price()}\n'
                     f'Состав : {', '.join(self.model.get_ingredients())}')
        return roll_data

    def site_restaurant_menu(self):
        roll_data = (f'Роллы : {self.model.get_name()}\n'
                     f'Вес 1 штуки : {self.model.get_weight()}'
                     f'Количество : {self.model.get_quantity()}\n'
                     f'Цена : {self.model.get_price()}\n'
                     f'Состав : {', '.join(self.model.get_ingredients())}'
                     f'Фото : {self.model.get_picture()}')
        return roll_data

    def set_ingredients(self,user_rights, new_ingredients: list):
        if user_rights in ['Director','Admin','IsStaff']:
            self.model.set_ingredients(new_ingredients)
            return 'Рецепт изменен!'
        else:
            return 'forbidden'

    def set_quantity(self, user_rights, new_quantity: int):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_quantity(new_quantity)
            return 'Количество изменено!'
        else:
            return 'У вас нет права доступа :('

    def set_weight(self, user_rights, new_weight: int):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_weight(new_weight)
            return 'Вес изменён!'
        else:
            return 'У вас нет права доступа :('

    def set_price(self, user_rights, new_price: int):
        if user_rights in ['Director', 'Admin', 'IsStaff']:
            self.model.set_price(new_price)
            return 'Цена измененa!'
        else:
            return 'У вас нет права доступа :('

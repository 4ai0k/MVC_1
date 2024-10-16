class RollsView:

    def __init__(self, controller):
        self.controller = controller

    def print_restaurant_menu(self):
        print(self.controller.restaurant_menu())

    def print_site_restaurant_menu(self):
        print(self.controller.site_restaurant_menu())

    def set_ingredients(self, user_rights, new_ingredients):
        if type(new_ingredients) is not list:
            print('Неверный тип данных!')
        elif self.controller.set_ingredients(user_rights, new_ingredients) == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(self.controller.set_ingredients(user_rights, new_ingredients))

    def set_quantity(self, user_rights, new_quantity):
        if type(new_quantity) is not int:
            print('Неверный тип данных!')
        elif self.controller.set_quantity(user_rights, new_quantity) == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(self.controller.set_quantity(user_rights, new_quantity))

    def set_weight(self, user_rights, new_weight):
        if type(new_weight) is not float:
            print('Неверный тип данных!')
        elif self.controller.set_weight(user_rights, new_weight) == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(self.controller.set_weight(user_rights, new_weight))

    def set_price(self, user_rights, new_price):
        if type(new_price) is not float:
            print('Неверный тип данных!')
        elif self.controller.set_price(user_rights, new_price) == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(self.controller.set_price(user_rights, new_price))

    def set_picture(self, user_rights, new_picture):
        if type(new_picture) is not str:
            print('Неверный тип данных!')
        elif self.controller.set_picture(user_rights, new_picture) == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(self.controller.set_picture(user_rights, new_picture))

    def save_order_to_json(self, order):
        print(self.controller.save_order_to_json(order))

    def get_data_from_json(self, user_rights, order):
        if self.controller.get_data_from_json(user_rights, order) == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(self.controller.get_data_from_json(user_rights,order))
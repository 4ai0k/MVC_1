class RollsViews:

    def __init__(self, controller):
        self.controller = controller

    def print_restaurant_menu(self):
        print(self.controller.restaurant_menu())

    def print_site_restaurant_menu(self):
        print(self.controller.site_restaurant_menu())

    def set_ingredients(self, user_rights, new_ingredients):
        set_ing = self.controller.set_ingredients(user_rights, new_ingredients)
        if  set_ing == 'Type error':
            print('Неверный тип данных!')
        elif set_ing == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(set_ing)

    def set_quantity(self, user_rights, new_quantity):
        set_quan = self.controller.set_quantity(user_rights, new_quantity)
        if set_quan == 'Type error':
            print('Неверный тип данных!')
        elif set_quan == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(set_quan)

    def set_weight(self, user_rights, new_weight):
        set_we = self.controller.set_weight(user_rights, new_weight)
        if set_we == 'Type error':
            print('Неверный тип данных!')
        elif set_we == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(set_we)

    def set_price(self, user_rights, new_price):
        set_pr = self.controller.set_price(user_rights, new_price)
        if set_pr == 'Type error':
            print('Неверный тип данных!')
        elif set_pr == 'forbidden':
            print('У вас нет права доступа :(')
        else:
            print(set_pr)
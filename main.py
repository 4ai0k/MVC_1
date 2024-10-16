import os
from models.RollsModel import RollsModel
from controllers.RollsController import RollsController
from views.RollsViews import RollsView

if __name__ == '__main__':
    rolls_model = RollsModel(name='Кани темпура',
        ingredients=['рис отварной', 'кляр', 'крабовые сурими',
                    'майонез', 'сыр творожный', 'соль пищевая', 'сухари панировочные'],
        weight=176.5,
        quantity=6,
        price=375.5,
        picture=os.path.abspath('images/rolls.webp'),
        client_ingredients=['больше сыра', 'больше огурца']
    )
    rolls_controller = RollsController(rolls_model)
    rolls_view = RollsView(rolls_controller)
    rolls_view.print_restaurant_menu()
    print()
    rolls_view.print_site_restaurant_menu()
    print()
    rolls_view.save_order_to_json('Кани темпура Клиента')
    print()
    rolls_view.get_data_from_json('user', r'orders\1729094032.74_Кани темпура Клиента')
    rolls_view.get_data_from_json('Admin',r'orders\1729094032.74_Кани темпура Клиента')
    # rolls_view.set_ingredients('user', ['свежий огурец', 'авокадо',
    #                                      'рис', 'соль', 'сахар', 'лист нори', 'рисовый уксус',
    #                                      'сыр «Филадельфия»', 'лосось малосолёный'])
    # rolls_view.set_ingredients('Admin', ['свежий огурец', 'авокадо',
    #                             'рис', 'соль', 'сахар', 'лист нори', 'рисовый уксус',
    #                             'сыр «Филадельфия»', 'лосось малосолёный'])
    # rolls_view.set_ingredients('Admin', 54353)
    # rolls_view.set_quantity('Admin',8)
    # rolls_view.set_weight('Admin',150.0)
    # rolls_view.set_price('Admin',504.3)
    # rolls_view.set_picture('user', os.path.abspath('images/rolls_2.webp'))
    # rolls_view.set_picture('Admin', os.path.abspath('images/rolls_2.webp'))
    # rolls_view.print_site_restaurant_menu()

import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes


STUB_PIZZA_1 = ttypes.Pizza(1, 'sample-image.png', ['peppers', 'cheese'])
STUB_PIZZA_2 = ttypes.Pizza(1, 'sample-image2.png', ['tomatos', 'cheese'])

class PizzasRepository(object):
    def get_available_pizzas():
        return {
            'margaritta': STUB_PIZZA_1,
            'martinitta': STUB_PIZZA_2
        }

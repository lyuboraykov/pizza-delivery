import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

from lib.db import db


class PizzasRepository(object):

    @classmethod
    def get_available_pizzas(cls):
        pizzas_dict = db.get('/pizzas', None)
        pizzas = {}
        for pizza_id, pizza_dict in enumerate(pizzas_dict):
            if not pizza_dict:
                continue
            pizzas[str(pizza_id)] = cls._get_pizza_from_dict(pizza_id, pizza_dict)
        return pizzas

    @classmethod
    def _get_pizza_from_dict(cls, pizza_id, pizza_dict):
        pizza = ttypes.Pizza(int(pizza_id),
                             pizza_dict['imageUrl'],
                             pizza_dict['products'])
        return pizza

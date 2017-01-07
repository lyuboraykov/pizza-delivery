import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

from lib.db import db


class PizzasRepository(object):

    @classmethod
    def get_available_pizzas(cls):
        pizzas_dict = db.get('/pizzas', None)
        pizzas = {}
        for pizza_id, pizza_dict in pizzas_dict.iteritems():
            if not pizza_dict:
                continue
            pizzas[pizza_id.encode('utf-8')] = cls._get_pizza_from_dict(pizza_dict)
        return pizzas

    @classmethod
    def _get_pizza_from_dict(cls, pizza_dict):
        pizza = ttypes.Pizza(int(pizza_dict['id']),
                            pizza_dict['imageUrl'],
                            [p.encode('utf-8') for p in pizza_dict['products']])
        return pizza

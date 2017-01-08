import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

from lib.db import db


class PizzasRepository(object):
    """Access to all operations related to the Pizza entity"""

    @classmethod
    def get_available_pizzas(cls):
        """Return all available pizzas

        :return dict<string, ttypes.Pizza>:
        """
        pizzas_dict = db.get('/pizzas', None)
        pizzas = {}
        for pizza_id, pizza_dict in pizzas_dict.iteritems():
            if not pizza_dict:
                continue
            pizzas[pizza_id.encode('utf-8')] = cls._dict_to_pizza(pizza_dict)
        return pizzas

    @classmethod
    def _dict_to_pizza(cls, pizza_dict):
        """Get a ttypes.Pizza from a dict representation"""
        pizza = ttypes.Pizza(int(pizza_dict['id']),
                             pizza_dict['imageUrl'],
                             [p.encode('utf-8') for p in pizza_dict['products']])
        return pizza

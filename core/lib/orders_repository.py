import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

from lib.db import db

STUB_ORDER_1 = ttypes.Order(1,
                            'Lyubo',
                            'Raykov',
                            'village Rahovtsi',
                            '0886108208',
                            1,
                            ttypes.OrderStatus.COOKING)

STUB_ORDER_2 = ttypes.Order(2,
                            'Martin',
                            'Hristov',
                            'Dryanovo',
                            '0895181786',
                            2,
                            ttypes.OrderStatus.DELIVERING)

class OrdersRepository(object):

    @classmethod
    def get_order_by_id(cls, order_id):
        order_dict = db.get('/orders', order_id)
        return cls._get_order_from_dict(order_id, order_dict)

    @classmethod
    def _get_order_from_dict(cls, order_id, order_dict):
        order = ttypes.Order(order_id,
                             order_dict['firstName'],
                             order_dict['lastName'],
                             order_dict['deliveryAddress'],
                             order_dict['phonenumber'],
                             int(order_dict['pizzaId']),
                             cls._get_status_enum_val_from_name(
                                 order_dict['status']))
        return order

    @classmethod
    def get_all_orders(cls):
        orders_dict = db.get('/orders', None)
        orders = []
        for order_id, order_dict in enumerate(orders_dict):
            if not order_dict:
                continue
            orders.append(cls._get_order_from_dict(int(order_id),
                                                   order_dict))
        return orders

    @classmethod
    def make_order(cls, order_req):
        return STUB_ORDER_1

    @classmethod
    def _get_status_enum_val_from_name(cls, status):
        return ttypes.OrderStatus._NAMES_TO_VALUES[status]

    @classmethod
    def _get_status_enum_name_from_val(cls, val):
        return ttypes.OrderStatus._VALUES_TO_NAMES[val]

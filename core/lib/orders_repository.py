import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

from lib.db import db

STUB_ORDER_1 = ttypes.Order(1,
                            'Lyubo',
                            'village Rahovtsi',
                            '0886108208',
                            1,
                            ttypes.OrderStatus.COOKING)

STUB_ORDER_2 = ttypes.Order(2,
                            'Martin',
                            'Dryanovo',
                            '0895181786',
                            2,
                            ttypes.OrderStatus.DELIVERING)

class OrdersRepository(object):

    @classmethod
    def get_order_by_id(cls, order_id):
        order_dict = db.get('/orders', order_id)
        return cls._order_from_dict(order_id, order_dict)

    @classmethod
    def _order_from_dict(cls, order_id, order_dict):
        order = ttypes.Order(order_id,
                             order_dict['name'],
                             order_dict['deliveryAddress'],
                             order_dict['phonenumber'],
                             int(order_dict['pizzaId']),
                             cls._get_status_enum_val_from_name(
                                 order_dict['status']))
        return order

    @classmethod
    def _dict_from_order(cls, order):
        return {
            'id': order.id,
            'name': order.name,
            'deliveryAddress': order.deliveryAddress,
            'phonenumber': order.phoneNumber,
            'pizzaId': order.pizzaId,
            'status': cls._get_status_enum_name_from_val(order.status)
        }

    @classmethod
    def get_all_orders(cls):
        orders_dict = db.get('/orders', None)
        orders = []
        for order_id, order_dict in enumerate(orders_dict):
            if not order_dict:
                continue
            orders.append(cls._order_from_dict(int(order_id),
                                                   order_dict))
        return orders

    @classmethod
    def make_order(cls, order_req):
        all_orders = cls.get_all_orders()
        new_id = len(all_orders) + 1
        order = ttypes.Order(
            id=new_id,
            name=order_req.name,
            deliveryAddress=order_req.deliveryAddress,
            phoneNumber=order_req.phoneNumber,
            pizzaId=order_req.pizzaId,
            status=ttypes.OrderStatus.PENDING
        )
        order_dict = cls._dict_from_order(order)
        db.put('/orders/', new_id, order_dict)
        return order

    @classmethod
    def _get_status_enum_val_from_name(cls, status):
        return ttypes.OrderStatus._NAMES_TO_VALUES[status]

    @classmethod
    def _get_status_enum_name_from_val(cls, val):
        return ttypes.OrderStatus._VALUES_TO_NAMES[val]

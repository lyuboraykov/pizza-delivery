import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

from lib.db import db


class OrdersRepository(object):

    @classmethod
    def get_order_by_id(cls, order_id):
        order_dict = db.get('/orders', order_id)
        return cls._dict_to_order(order_id, order_dict)

    @classmethod
    def get_all_orders(cls):
        orders_dict = db.get('/orders', None)
        orders = []
        for order_id, order_dict in enumerate(orders_dict):
            if not order_dict:
                continue
            orders.append(cls._dict_to_order(int(order_id),
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
        cls._set_order_by_id(new_id, order)
        return order

    @classmethod
    def update_order_status(cls, order_id, status):
        order = cls.get_order_by_id(order_id)
        order.status = status
        cls._set_order_by_id(order_id, order)
        return order

    @classmethod
    def _get_status_enum_val_from_name(cls, status):
        return ttypes.OrderStatus._NAMES_TO_VALUES[status]

    @classmethod
    def _get_status_enum_name_from_val(cls, val):
        return ttypes.OrderStatus._VALUES_TO_NAMES[val]

    @classmethod
    def _set_order_by_id(cls, order_id, order):
        order_dict = cls._order_to_dict(order)
        db.put('/orders/', order_id, order_dict)

    @classmethod
    def _dict_to_order(cls, order_id, order_dict):
        order = ttypes.Order(order_id,
                             order_dict['name'].encode('utf-8'),
                             order_dict['deliveryAddress'].encode('utf-8'),
                             order_dict['phonenumber'],
                             int(order_dict['pizzaId']),
                             cls._get_status_enum_val_from_name(
                                 order_dict['status']))
        return order

    @classmethod
    def _order_to_dict(cls, order):
        return {
            'id': order.id,
            'name': order.name,
            'deliveryAddress': order.deliveryAddress,
            'phonenumber': order.phoneNumber,
            'pizzaId': order.pizzaId,
            'status': cls._get_status_enum_name_from_val(order.status)
        }

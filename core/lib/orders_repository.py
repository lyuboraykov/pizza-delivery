import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

from lib.db import db


class OrdersRepository(object):
    """Access to all operations related to orders"""

    @classmethod
    def get_order_by_id(cls, order_id):
        """Return an order with this id"""
        order_dict = db.get('/orders', order_id)
        return cls._dict_to_order(order_id, order_dict)

    @classmethod
    def get_all_orders(cls):
        """Return a list of all orders in the database"""
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
        """Create a new order and return it"""
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
        """Change the status of an existing order"""
        order = cls.get_order_by_id(order_id)
        order.status = status
        cls._set_order_by_id(order_id, order)
        return order

    @classmethod
    def _status_name_to_val(cls, status):
        """Get the value of an order status from its name"""
        return ttypes.OrderStatus._NAMES_TO_VALUES[status]

    @classmethod
    def _status_val_to_name(cls, val):
        """Get the name of a status from its value"""
        return ttypes.OrderStatus._VALUES_TO_NAMES[val]

    @classmethod
    def _set_order_by_id(cls, order_id, order):
        """Set an order in the database by id

        Create a new one if non-existent, override else
        """
        order_dict = cls._order_to_dict(order)
        db.put('/orders/', order_id, order_dict)

    @classmethod
    def _dict_to_order(cls, order_id, order_dict):
        """Convert an order dict ot ttypes.Order"""
        order = ttypes.Order(order_id,
                             order_dict['name'].encode('utf-8'),
                             order_dict['deliveryAddress'].encode('utf-8'),
                             order_dict['phonenumber'],
                             int(order_dict['pizzaId']),
                             cls._status_name_to_val(
                                 order_dict['status']))
        return order

    @classmethod
    def _order_to_dict(cls, order):
        """Get a dict representation of an order"""
        return {
            'id': order.id,
            'name': order.name,
            'deliveryAddress': order.deliveryAddress,
            'phonenumber': order.phoneNumber,
            'pizzaId': order.pizzaId,
            'status': cls._status_val_to_name(order.status)
        }

import sys

sys.path.append('../gen-py')

from pizza_delivery import ttypes

STUB_ORDER_1 = ttypes.Order(1,
                            'Lyubo',
                            'Raykov',
                            'village Rahovtsi',
                            '0886108208',
                            1,
                            ttypes.OrderStatus.IN_PROGRESS)

STUB_ORDER_2 = ttypes.Order(2,
                            'Martin',
                            'Hristov',
                            'Dryanovo',
                            '0895181786',
                            2,
                            ttypes.OrderStatus.ACCEPTED)

class OrdersRepository(object):

    @classmethod
    def get_order_by_id(cls, id):
        return STUB_ORDER_1

    @classmethod
    def get_all_orders(cls):
        return [STUB_ORDER_1, STUB_ORDER_2]

    @classmethod
    def make_order(cls, order_req):
        return STUB_ORDER_1

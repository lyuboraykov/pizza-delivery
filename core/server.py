#!/usr/bin/env python

import sys

from thrift.transport import TSocket
from thrift.transport import TTransport

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
sys.path.append('gen-py')

from pizza_delivery import (
    PizzaDelivery,
    ttypes
)

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

STUB_PIZZA_1 = ttypes.Pizza(1, 'sample-image.png', ['peppers', 'cheese'])
STUB_PIZZA_2 = ttypes.Pizza(1, 'sample-image2.png', ['tomatos', 'cheese'])


class PizzaDeliveryHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        return "pong"

    def getOrderById(self, id):
        return STUB_ORDER_1

    def getAllOrders(self):
        return [STUB_ORDER_1, STUB_ORDER_2]

    def makeOrder(self, order_req):
        return STUB_ORDER_1

    def getAvailablePizzas(self):
        return {
            'margaritta': STUB_PIZZA_1,
            'martinitta': STUB_PIZZA_2
        }


handler = PizzaDeliveryHandler()
processor = PizzaDelivery.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()
print "done!"

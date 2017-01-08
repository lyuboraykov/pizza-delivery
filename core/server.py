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

from lib.orders_repository import OrdersRepository
from lib.pizzas_repository import PizzasRepository
import logging

logging.basicConfig(level=logging.DEBUG)

class PizzaDeliveryHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        """"Health check of the service"""
        return "pong"

    def getOrderById(self, id):
        """Get an order by id"""
        return OrdersRepository.get_order_by_id(id)

    def getAllOrders(self):
        """Retrieve all orders"""
        return OrdersRepository.get_all_orders()

    def makeOrder(self, order_req):
        """Create a new order"""
        return OrdersRepository.make_order(order_req)

    def updateOrderStatus(self, id, status):
        """Change the status of an order"""
        return OrdersRepository.update_order_status(id, status)

    def getAvailablePizzas(self):
        """Get all available pizzas"""
        return PizzasRepository.get_available_pizzas()


handler = PizzaDeliveryHandler()
processor = PizzaDelivery.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()

#!/usr/bin/env python

import sys

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

sys.path.append('gen-py')

from pizza_delivery import (
    PizzaDelivery,
    ttypes
)


try:
    transport = TSocket.TSocket('localhost', 30303)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = PizzaDelivery.Client(protocol)
    transport.open()
    print 'Pinging...'
    print client.ping()
    print 'Retrieving order with id 1...'
    print client.getOrderById(1)
    print 'Retrieving all orders...'
    print client.getAllOrders()
    print 'Retrieving available pizzas...'
    print client.getAvailablePizzas()

    print 'Making an order...'
    order_req = ttypes.OrderRequest(
        name='lyubo',
        deliveryAddress='test address',
        phoneNumber='0881 11 22 33',
        pizzaId=1
    )
    new_order = client.makeOrder(order_req)
    print new_order

    print 'Updating the new order status...'
    client.updateOrderStatus(new_order.id, ttypes.OrderStatus.COOKING)

    transport.close()
    print 'Done!'

except Thrift.TException, tx:
    print "%s" % tx.message

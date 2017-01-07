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
    print client.ping()
    print client.getOrderById(1)
    print client.getAllOrders()
    print client.getAvailablePizzas()
    transport.close()

except Thrift.TException, tx:
    print "%s" % tx.message

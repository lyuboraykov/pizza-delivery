#!/usr/bin/env python

import sys

from thrift.transport import TSocket
from thrift.transport import TTransport

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
sys.path.append('gen-py')

from pizza_delivery import PizzaDelivery


class PizzaDeliveryHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        return "pong"

    def say(self, msg):
        print msg


handler = PizzaDeliveryHandler()
processor = PizzaDelivery.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()
print "done!"

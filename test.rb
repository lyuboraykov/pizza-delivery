require_relative 'gen-rb/pizza_delivery'

  begin
    port = 30303

    transport = Thrift::BufferedTransport.new(Thrift::Socket.new('localhost', port))
    protocol = Thrift::BinaryProtocol.new(transport)
    client = PizzaDelivery::Client.new(protocol)

    transport.open()

    p client.getAllOrders()

  rescue Thrift::Exception => tx
    print 'Thrift::Exception: ', tx.message, "\n"
  end
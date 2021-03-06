class RpcCaller
  def self.call_method method_name, arguments
    begin
      port = 30303

      transport = Thrift::BufferedTransport.new(Thrift::Socket.new('localhost', port))
      protocol = Thrift::BinaryProtocol.new(transport)
      client = PizzaDelivery::Client.new(protocol)

      transport.open()

      if arguments
        result = client.method(method_name).call(*arguments)
      else
        result = client.method(method_name).call
      end
      transport.close()

      result
    rescue Thrift::Exception => tx
      print 'Thrift::Exception: ', tx.message, "\n"
    end
  end
end
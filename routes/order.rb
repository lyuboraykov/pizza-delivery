require_relative '../gen-rb/pizza_delivery'

post '/order' do

  # begin
  #   port = 30303

  #   transport = Thrift::BufferedTransport.new(Thrift::Socket.new('localhost', port))
  #   protocol = Thrift::BinaryProtocol.new(transport)
  #   client = PizzaDelivery::Client.new(protocol)

  #   transport.open()

  #   client.ping()

  # rescue Thrift::Exception => tx
  #   print 'Thrift::Exception: ', tx.message, "\n"
  # end
end

get '/orders/:order_id' do
  order_id = params['order_id']

  # get order by id and send status to view

  erb :customer_status
end

get '/update_status/:order_id' do
  'test'
end
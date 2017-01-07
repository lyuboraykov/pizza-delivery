post '/order' do
  # perform call to the thrift and return an order ID
  puts params

  "1"
end

get '/orders/:order_id' do
  order_id = params['order_id']

  # get order by id and send status to view

  erb :customer_status
end

get '/update_status/:order_id' do
  'test'
end
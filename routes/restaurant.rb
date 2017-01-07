get '/restaurant' do
  orders = RpcCaller::call_method :getAllOrders, nil

  erb :restaurant, locals: { orders: orders }
end
get '/restaurant' do
  orders = RpcCaller::call_method :getAllOrders, nil

  p orders

  erb :restaurant
end
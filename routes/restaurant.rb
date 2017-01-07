get '/restaurant' do
  orders = Hash.new

  erb :restaurant, locals: {orders: orders}
end
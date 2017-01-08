require 'json'

get '/restaurant' do
  orders = RpcCaller::call_method :getAllOrders, nil
  pizzas = RpcCaller::call_method :getAvailablePizzas, nil

  erb :restaurant, locals: { orders: orders, pizzas: pizzas }
end

get '/orders/:order_id' do
  order = RpcCaller::call_method :getOrderById, params['order_id'].to_i

  response_json = {
    name: order.name,
    deliveryAddress: order.deliveryAddress,
    phoneNumber: order.phoneNumber,
    status: order.status,
    pizzaName: pizza_by_id(order.pizzaId)[:name],
    pizzaSrc: pizza_by_id(order.pizzaId)[:src]
  }

  response_json.to_json
end

put '/orders/:order_id' do
  order = RpcCaller::call_method :updateOrderStatus, ([params['order_id'].to_i, params['statusIndex'].to_i])
end

def pizza_by_id id
  pizzas = RpcCaller::call_method :getAvailablePizzas, nil
  result = {}
  pizzas.keys.each do |key|
    if pizzas[key].id == id
      result[:name] = key
      result[:src] = pizzas[key].imageUrl
    end
  end
  result
end
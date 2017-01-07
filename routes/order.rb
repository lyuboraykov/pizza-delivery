require_relative '../gen-rb/pizza_delivery'
require_relative '../helpers/rpc_caller'

post '/order' do
    order_settings = params
    order_settings["pizzaId"] = order_settings["pizzaId"].to_i
    order_request = OrderRequest.new order_settings

    order = RpcCaller::call_method :makeOrder, order_request

    order.id.to_s
end

get '/orders/:order_id/view' do
  order_id = params['order_id'].to_i
  order = RpcCaller::call_method :getOrderById, order_id

  erb :customer_status, locals: { order: order }
end

get '/update_status/:order_id' do
  order_id = params['order_id'].to_i

  order = RpcCaller::call_method :getOrderById, order_id

  order.status.to_s
end
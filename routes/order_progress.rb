get '/order_progress' do
  erb :order_progress
end

post '/order' do
  puts params
end
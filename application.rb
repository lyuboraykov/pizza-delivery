require 'sinatra'
require 'thrift'

require_relative 'routes/customer'
require_relative 'routes/order'
require_relative 'routes/restaurant'

get '/' do
  redirect '/customer'
end
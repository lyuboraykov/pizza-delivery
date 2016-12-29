require 'sinatra'

# require_relative 'routes/users'

enable :sessions

get '/' do
  erb :home
end

# DataMapper.auto_upgrade!

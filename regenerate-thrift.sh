cd core
thrift -r --gen py pizza_delivery.thrift

cd ..
thrift -r --gen rb core/pizza_delivery.thrift

RUBY_GEN_DELIVERY='gen-rb/pizza_delivery.rb'

sed -i -e '8 s/require/require_relative/' $RUBY_GEN_DELIVERY

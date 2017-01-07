enum OrderStatus {
    PENDING
    COOKING
    QUALITY_CONTROL
    DELIVERING
    ON_DESTINATION
}

struct Order {
    1: required i32 id
    2: required string name
    4: required string deliveryAddress
    5: required string phoneNumber
    6: required i32 pizzaId
    7: required OrderStatus status
}

struct OrderRequest {
    1: required string name
    2: required string deliveryAddress
    3: required string phoneNumber
    4: required i32 pizzaId
}

struct Pizza {
    1: required i32 id
    2: required string imageUrl
    3: required list<string> products
}

service PizzaDelivery {
    string ping()

    Order makeOrder(
        1: OrderRequest order
    )

    Order getOrderById(
        1: i32 id
    )

    list<Order> getAllOrders()

    Order updateOrderStatus(
        1: i32 id
        2: OrderStatus status
    )

    map<string, Pizza> getAvailablePizzas()
}

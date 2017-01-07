enum OrderStatus {
    PENDING
    COOKING
    QUALITY_CONTROL
    DELIVERING
    ON_DESTINATION
}

struct Order {
    1: required i32 id
    2: required string firstName
    3: required string lastName
    4: required string deliveryAddress
    5: required string phoneNumber
    6: required i32 pizzaId
    7: required OrderStatus status
}

struct OrderRequest {
    1: required string firstName
    2: required string lastName
    3: required string deliveryAddress
    4: required string phoneNumber
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

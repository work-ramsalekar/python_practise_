from cust import Customer
from Carts import cart


class main :
    cart1 = cart(["soap","brush"], 200)
    customer1 = Customer(1,"rock","123",cart1)

    print(customer1)



    
class Order:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    
    def get_total(self):
        return self.price * self.quantity

class Customer:
    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.orders = []
    
    def make_order(self, order):
        self.orders.append(order)

    def display_greeting(self):
        if self.age < 18:
            return("Дорогой юный друг, добро пожаловать")
        else:
            return(f"Добрый день, {self.name}")
    
    def get_order_history(self):
        for order in self.orders:
            print(f"Куплен {order.product_name} в количестве {order.quantity}")

class VIPClient(Customer):
    def __init__(self, name, age, email, password, status):
        Customer.__init__(self, name, age, email, password)
        self.status = status

    def display_greeting(self):
        return(f"Добрый день, уважаемый {self.name}, ваш ВИП статус равен {self.status}")

newCustomer = Customer("Петр",25,"example@example.com","password")
print(newCustomer.display_greeting())
order1 = Order("Книга",50,2)
order2 = Order("Пуховик",400,1)
newCustomer.make_order(order1)
newCustomer.make_order(order2)
newCustomer.get_order_history()

newVipCustomer = VIPClient("Федор",35,"example@example.com","password",2)
order3 = Order("Книга",50,3)
newVipCustomer.make_order(order3)
newVipCustomer.get_order_history()
print(newVipCustomer.display_greeting())
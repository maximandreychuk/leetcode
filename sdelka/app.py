from abc import ABCMeta, abstractmethod


class Client:
    def __init__(self, client_type):
        self.client_type = client_type


class Order:
    def __init__(self, client, discount_applicator):
        self.client = client
        self.discount_applicator = discount_applicator
        self.items = []
        self.final_price = None

    def add_item(self, order_item):
        self.items.append(order_item)

    def get_final_price(self):
        return self.discount_applicator.get_adjusted_price(self)


class OrderItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price


class DiscountApplicator(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_adjusted_price(self, order):
        pass


class NoDiscountApplicator(DiscountApplicator):
    def __init__(self):
        DiscountApplicator.__init__(self)

    def get_adjusted_price(self, order):
        accumulator = 0
        for order_item in order.items:
            accumulator += order_item.item_price

        return accumulator


class CorporateDiscountApplicator(DiscountApplicator):
    def __init__(self):
        DiscountApplicator.__init__(self)

    def get_adjusted_price(self, order):
        accumulator = 0
        for order_item in order.items:
            if order_item.item_name == "Car":
                accumulator += order_item.item_price * 0.8
            else:
                accumulator += order_item.item_price * 0.9

        return accumulator


class StandardDiscountApplicator(DiscountApplicator):
    def __init__(self):
        DiscountApplicator.__init__(self)

    def get_adjusted_price(self, order):
        accumulator = 0
        for order_item in order.items:
            accumulator += order_item.item_price * 0.95

        return accumulator


class DiscountApplicatorSource:
    def __init__(self):
        pass

    @staticmethod
    def get_discount_applicator(client):
        if client.client_type == "standard":
            return StandardDiscountApplicator()
        elif client.client_type == "corporate":
            return CorporateDiscountApplicator()
        else:
            return NoDiscountApplicator()


if __name__ == "__main__":
    joe = Client("corporate")
    discount_applicator = \
        DiscountApplicatorSource.get_discount_applicator(joe)

    car = OrderItem("Car", 10000)
    computer = OrderItem("Computer", 1000)
    pen = OrderItem("Pen", 10)

    order = Order(joe, discount_applicator)
    order.add_item(car)
    order.add_item(computer)
    order.add_item(pen)

    final_price = order.get_final_price()
    print(f"Final price: {final_price}")
#!/usr/bin/python3

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# class Promotion(ABC):

    # @abstractmethod
class Promotion(ABC):

    @abstractmethod
    def discount(order):
        ''' 返回折扣金额（正值）'''
        pass


class FidelityPromo(Promotion):
    '''为1000积分以上的顾客5%折扣'''

    def discount(order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    '''单个商品20个或以上时10%折扣'''

    def discount(order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    '''订单不同的商品达到10个或以上时提供7%折扣'''

    def discount(order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


def test():
    joe = Customer('john', 0)
    ann = Customer('Ann', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)
    ]
    print(Order(joe, cart))
    o = Order(joe, cart)
    FidelityPromo.discount(o)

    print(Order(joe, cart, FidelityPromo))
    print(Order(ann, cart, FidelityPromo))

    banana_cart = [
        LineItem('banana', 34, .5),
        LineItem('apple', 10, 1.5),
    ]
    print(Order(joe, banana_cart, BulkItemPromo))
    print(Order(ann, banana_cart, BulkItemPromo))

    long_cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]    
    print(Order(joe, long_cart, LargeOrderPromo))
    print(Order(ann, long_cart, LargeOrderPromo))

    
if __name__ == "__main__":
    test()


def fidel_promo(order):
    '''为1000积分以上的顾客5%折扣'''
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulkItem_promo(order):
    '''单个商品20个或以上时10%折扣'''

    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def largeOrder_promo(order):
    '''订单不同的商品达到10个或以上时提供7%折扣'''

    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0

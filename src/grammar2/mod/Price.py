def price1(price, discount):
    newPrice = ('{:.2f}'.format(price * discount / 10))
    return newPrice


def price2(price):
    if price > 88:
        newPrice = ('{:.2f}'.format(price * 0.9))
    elif price > 188:
        newPrice = ('{:.2f}'.format(price * 0.8))
    elif price > 288:
        newPrice = ('{:.2f}'.format(price * 0.8))
    else:
        newPrice = price
    return newPrice

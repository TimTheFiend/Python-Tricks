def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    """Assert:
                If this isn't true, throw an exception
    """
    try:
        assert 0 <= price <= product['price']
    except AssertionError:
        return "The discount is so low we're giving people money to buy them"
    return price

shoes = {'name': 'Fancy shoes', 'price': 14900}
foobar = apply_discount(shoes, 1.0)
print(foobar)
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    """Assert:
                If this isn't true, throw an exception

        Assertions are meant to be internal self-checks for you program.
        They work by declaring some conditions as impossible in your code.
        If one of these conditions doesn't hold, that means there's a bug in the program.

        If your program is bug-free, these conditions will never occur.
        But if they do occur, the program will crash with an assertion error telling you exactly which
        "impossible" condition was triggered. This makes it much easier to track down and fix bugs in your program.

        Keep in mind that assert statements is a debugging aid, not a mechanism for handling run-time errors.
    """
    try:
        assert 0 <= price <= product['price']
    except AssertionError:
        return "The discount is so low we're giving people money to buy them"
    return price

shoes = {'name': 'Fancy shoes', 'price': 14900}
foobar = apply_discount(shoes, 1.0)
print(foobar)
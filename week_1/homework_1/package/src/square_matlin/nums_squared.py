def numbers_added_and_squared(x, y):
    if isinstance(x, int) or isinstance(y, int):
        return (x + y) * (x + y)
    else:
        raise TypeError

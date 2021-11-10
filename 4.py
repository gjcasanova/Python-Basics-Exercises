import doctest


def leapyear(y):
    """
    >>> leapyear(1999)
    False
    >>> leapyear(1968)
    True
    >>> leapyear(2000)
    True
    >>> leapyear(1800)
    False
    """
    if (y % 100 != 0 and y % 4 == 0) or (y % 400 == 0):
        return True
    return False


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

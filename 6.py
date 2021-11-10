import doctest


def update_arrival(h, m, d):
    """
    >>> update_arrival(10, 45, 20)
    (11, 5)
    >>> update_arrival(12, 30, 60)
    (13, 30)
    >>> update_arrival(22, 0, 120)
    (0, 0)
    >>> update_arrival(23, 57, 5 + 24*60)
    (0, 2)
    """
    extra_hours, minutes = divmod((m + d), 60)
    hours = (extra_hours + h) % 24
    return (hours, minutes)


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

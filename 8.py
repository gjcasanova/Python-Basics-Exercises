import doctest


def add1sec(h, m, s):
    """
    >>> add1sec(0, 1, 2)
    (0, 1, 3)
    >>> add1sec(3, 5, 9)
    (3, 5, 10)
    >>> add1sec(19, 45, 59)
    (19, 46, 0)
    >>> add1sec(12, 59, 59)
    (13, 0, 0)
    """
    extra_minutes, seconds = divmod(s+1, 60)
    extra_hours, minutes = divmod(m+extra_minutes, 60)
    hours = (h+extra_hours) % 24
    return (hours, minutes, seconds)


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

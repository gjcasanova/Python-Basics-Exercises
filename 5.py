import doctest


def decompose(n):
    """
    >>> decompose(147)
    (0, 2, 27)
    >>> decompose(3661)
    (1, 1, 1)
    >>> decompose(76234)
    (21, 10, 34)
    """
    hours, seconds = divmod(n, 3600)
    minutes, seconds = divmod(seconds, 60)
    return (hours, minutes, seconds)


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

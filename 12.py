import doctest


def triangulo(side_a, side_b, side_c):
    """
    >>> triangulo(2, 3, 4)
    'escaleno'
    >>> triangulo(2, 2, 3)
    'isosceles'
    >>> triangulo(1, 1, 1)
    'equilatero'
    """
    if (side_a == side_b == side_c):
        return 'equilatero'
    if (side_a != side_b != side_c):
        return 'escaleno'
    return 'isosceles'


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

import doctest


def repago(person_type, revenue):
    """
    >>> repago('Pensionista', 5000)
    (10, 8.23)
    >>> repago('Pensionista', 180000)
    (60, 61.75)
    >>> repago('Usuario', 25000)
    (50, -1.0)
    >>> repago('Sin subsidio', 5000)
    (0, 0.0)
    """
    if person_type == 'Pensionista':
        if revenue < 18_000:
            return (10, 8.23)

        if 18_000 <= revenue < 100_000:
            return (10, 18.52)

        return (60, 61.75)

    if person_type == 'Usuario':
        if revenue < 18_000:
            return (40, -1.0)

        if 18_000 <= revenue < 100_000:
            return (50, -1.0)

        return (60, -1.0)

    return (0, 0.0)


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

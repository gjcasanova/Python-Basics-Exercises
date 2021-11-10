import doctest


def leading_hand(h, m):
    """
    >>> leading_hand(22, 51)
    'minute hand'
    >>> leading_hand(21, 45)
    'draw'
    >>> leading_hand(6, 28)
    'hour hand'
    >>> leading_hand(4, 20)
    'draw'
    """
    hour_angle = 30 * (h % 12)
    minute_angle = 6 * m

    return 'draw' if hour_angle == minute_angle else 'minute hand' if minute_angle > hour_angle else 'hour hand'

    return (0, 0.0)


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

import doctest


def winner(p, q, r, s):
    """
    >>> winner(1, 3, 5, 6)
    1
    >>> winner(2, 4, 4, 3)
    2
    >>> winner(1, 3, 2, 3)
    2
    >>> winner(2, 4, 3, 3)
    0
    >>> winner(4, 4, 5, 6)
    0
    """
    score_a, score_b = p+q, r+s
    if score_a == score_b or (score_a > 7 and score_b > 7):
        return 0

    return 1 if score_b > 7 or score_a > score_b else 2


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

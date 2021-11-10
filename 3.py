import doctest


def t_descubierto(timeline):
    events = [-1 if x == '-' else 1 for x in timeline]
    queue_length = 0
    result = 0
    for event in events:
        queue_length += event
        if queue_length > 3:
            result += 1
    return result


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

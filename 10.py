import doctest


def is_vowel_covered(s):
    """
    >>> is_vowel_covered('AaaaA')
    True
    >>> is_vowel_covered('AaaA')
    False
    >>> is_vowel_covered('AeioUAeioU')
    True
    >>> is_vowel_covered('aAppAlAa')
    False
    >>> is_vowel_covered('AaaaaazZ')
    False
    """
    if len(s) > 4:
        upper_vowels = 'AEIOU'
        lower_vowels = 'aeiou'

        return (s[0] in upper_vowels and s[-1] in upper_vowels) and (s[1] in lower_vowels and s[-2] in lower_vowels)

    return False


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

import string


# def regroup(s):
#     letters = ''
#     digits = ''
#     for l in s:
#         if l in string.ascii_lowercase:
#             letters += l
#         else:
#             digits += l
#     return letters + digits


# def regroup(s):
#     letters = ''
#     digits = ''
#     import string for l in s: if l in string.ascii_lowercase: letters += l else: digits += l return letters + digits

# def count_a(s, stop):
#     counter = 0
#     if stop not in s:
#         return -1
#     for c in s:
#         if c == stop:
#             break
#         if c == 'a':
#             counter += 1
#     return counter


# def count_a(s, stop):
#     counter = 0
#     found = False
#     if stop not in s:
#         return -1
#     for c in s:
#         if c == stop:
#             found = True
#         if c == 'a' and not found:
#             counter += 1
#     return counter


# def count_words(s):
#     counter = 0
#     fixed_s = ' ' + s

#     for idx in range(1, len(fixed_s)):  # 1, 2, 3... [len(fixed_s) - 1] => 'Hola' => ' Hola' => H O L A.
#         current = fixed_s[idx]  # Es el caracter actuar
#         pre = fixed_s[idx-1]  # Es el caracter anterior

#         if pre == ' ' and current != ' ':
#             counter += 1

#     return counter


# def count_words2(s):
#     counter = 0
#     fixed_s = ' ' + s

#     for idx, char in enumerate(fixed_s[1:]):  # 1, 2, 3... [len(fixed_s) - 1] => 'Hola' => ' Hola' => H O L A.
#         current = char  # Es el caracter actuar
#         pre = fixed_s[idx-1]  # Es el caracter anterior
#         if pre == ' ' and current != ' ':
#             counter += 1

#     return counter


def max_altura(s):
    max_value = 0
    dishes = 0
    for event in s:
        if event == '+':
            dishes += 1
        else:
            dishes -= 1

        # if max_value < dishes:
        #     max_value = dishes

        max_value = max(max_value, dishes)

    return max_value


print(max_altura('+++--+'))
print(max_altura('+-+-+-+-'))
print(max_altura('++-+++--+'))

# print(count_words2('Qui inventi  amicum inventin thesaurum'))
# print(count_words2('ales leta           est'))
# print(count_words2('KingKing'))

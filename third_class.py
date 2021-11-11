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
#         pre = fixed_s[idx]  # Es el caracter anterior
#         if pre == ' ' and current != ' ':
#             counter += 1

#     return counter


# def max_altura(s):
#     max_value = 0
#     dishes = 0
#     for event in s:
#         if event == '+':
#             dishes += 1
#         else:
#             dishes -= 1

#         # if max_value < dishes:
#         #     max_value = dishes

#         max_value = max(max_value, dishes)

#     return max_value


# print(max_altura('+++--+'))
# print(max_altura('+-+-+-+-'))
# print(max_altura('++-+++--+'))

# print(count_words2('Qui inventi  amicum inventin thesaurum'))
# print(count_words2('ales leta           est'))
# print(count_words2('KingKing'))


# def kth_word(s, k):
#     counter = 0
#     fixed_s = f' {s} '  # ' ' + s + ' '

#     pos_init = 0  # Voy a guardar la pos de la primera letra de la palabra kt
#     pos_end = 0  # Voy a guardar la pos de la ultima letra de la palabra kt

#     # Encontrar el inicio de la kt_word
#     for idx_i in range(1, len(s)-1):
#         # Obtengo la letra actual y la letra anterior a esa
#         current = fixed_s[idx_i]
#         pre = fixed_s[idx_i-1]

#         # Es el inicio de una nueva palabra?
#         if current != ' ' and pre == ' ':
#             counter += 1

#             if counter == k:
#                 pos_init = idx_i

#                 for idx_j in range(idx_i, len(fixed_s)):
#                     if fixed_s[idx_j] == ' ':
#                         pos_end = idx_j
#                         return fixed_s[pos_init: pos_end]
#     return ''


# print(kth_word('Alea iacta est', 3))
# print(kth_word('Alea iacta est', 1))
# print(kth_word('KingKong', 2))
# print(kth_word('KingK  ong', 2))
# print(kth_word('Kin  gK  ong', 2))
# print(kth_word('King   Ko   n   g     ', 4))


def perfect_number(n):
    counter = 0
    for i in range(1, n):
        if n % i == 0:
            counter += i

    return counter == n


print(perfect_number(6))
print(perfect_number(8))
print(perfect_number(28))
print(perfect_number(496))
print(perfect_number(1))

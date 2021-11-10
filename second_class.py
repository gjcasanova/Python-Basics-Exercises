# def leapyear(y):
#     return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


# def decompose(n):
#     minutes, seconds = n//60, n%60
#     hours, minutes = divmod(minutes, 60)
#     return hours, minutes, seconds


# def t_descubierto(s):
#     persons = 0
#     seconds = 0
#     for event in s:
#         if event == '+':
#             persons += 1
#         else:
#             persons -= 1
#         if persons > 3:
#             seconds += 1
#     return seconds


# def delete_repes(s):
#     result = ''
#     for letter in s:
#         if letter not in result:
#             result += letter
#     return result

# def vocales_andarinas(w):
#     result = ''
#     for vocal in w:
#         l = vocal
#         if vocal == 'a':
#             l = 'e'
#         if vocal == 'e':
#             l = 'i'
#         if vocal == 'i':
#             l = 'o'
#         if vocal == 'o':
#             l = 'u'
#         if vocal == 'u':
#             l = 'a'
#         result += l
#     return result

# print(vocales_andarinas('mi mama me mima'))


def slow_pi_approx(n):
    result = 0
    for k in range(0, n+1):
        partial = ((-1)**k)/(2*k + 1)
        result += partial
    return round(4*result, 4)


print(slow_pi_approx(10))
print(slow_pi_approx(100))
print(slow_pi_approx(1000))

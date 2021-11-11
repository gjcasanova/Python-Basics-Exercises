# def vuelve(orden):
#     pos_x = 0
#     pos_y = 0

#     for i in orden:
#         if i == 'n':
#             pos_y += 60
#         if i == 's':
#             pos_y -= 60
#         if i == 'e':
#             pos_x += 60
#         if i == 'o':
#             pos_x -= 60

#     return pos_x == pos_y == 0


# print(vuelve('nseo'))
# print(vuelve('nen'))

# def is_palindrom(s):
#     return s == s[::-1]

# def es_palindrom(s):
#     for i in range(len(s)//2):
#         j = -i-1
#         if s[i] != s[j]:
#             return False
#     return True

# def is_palindrom(s):
#     for i in range(len(s)//2):
#         j = -i - 1
#         if s[i] != s[j]:
#             return False
#     return True


# print(is_palindrom('xyzzyx'))
# print(is_palindrom('xyyx'))
# print(is_palindrom('xyzx'))
# print(is_palindrom('xyx'))
# print(is_palindrom('xyz'))


def empty_triangle(n): # 0, 1, 2... n-1
    # Primera fila
    print((n-1) * ' ' + '*')

    # Filas intermedias
    for x in range(1, n-1):
        initial_spaces = (n-x-1) * ' '
        empty_spaces = (2*x - 1) * ' '
        print(initial_spaces + '*' + empty_spaces + '*')
        # print(f'{initial_spaces}*{empty_spaces}*')

    # Ultima fila
    print((2*n-1) * '*')


empty_triangle(3)
print()
empty_triangle(5)
print()
empty_triangle(10)


# *
# **
# ***
# ****
# *****

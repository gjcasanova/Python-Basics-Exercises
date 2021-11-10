def triangulo(side_a, side_b, side_c):  # (3, 4, 4)
    if side_a == side_b == side_c:
        return 'equilatero'
    if side_a != side_b != side_c:
        return 'escaleno'
    else:
        return 'isosceles'

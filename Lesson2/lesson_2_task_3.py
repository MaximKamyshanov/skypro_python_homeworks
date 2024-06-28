import math

def square(side):
    if isinstance(side, int):
        return side ** 2
    else:
        return math.ceil(side ** 2)
    
side = float(input("Укажите длину стороны квадрата"))
area = square(side)
print(f"Площадь квадрата со стороной {side} равна {area}")

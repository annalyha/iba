#  Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.


def trib(n, c=1, p=0, pp=0):
    if (n == 0):
        return pp
    if (n == 1):
        return p
    if (n == 0):
        return c
    else:
        return trib(n - 1, c + p + pp, c, p)


print(trib(35))

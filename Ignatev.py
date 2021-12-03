

def time(key):
    import datetime
    key = datetime.datetime.now()
    key = str(key)
    print(key)
    return time

def pramoug(g):
    print("Площадь прямоугольника ")
    from math import tan, pi
    s = int(input())
    n = int(input())
    g = (n * s ** 2) / (4 + tan(pi / n))
    g = int(g)
    print(g)
    return g
def summ(func):
    print("Сумма n чисел ")
    n = int(input())
    s = (n * (n + 1)) / 2
    s = str(s)
    print(s)
    return s

while True:
    print("Привет выбери одну из двух программ")
    z = str(input())
    if z == "1":
        print("Выбранна программа")
        @time
        @pramoug
        def a():
            return
    elif z == "2":
        print("Выбранна программа")
        @time
        @summ
        def a():
            return
    elif z == "0":
        break
    else:
        print("вы ввели не правильное значение")

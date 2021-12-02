print("Выбор функции")
def vbor(t):

    def tnow():
                    '''Текущее время'''
                    import datetime
                    dt_now = datetime.datetime.now()
                    return 1

    def pramoug():
                    print("Площадь прямоугольника ")
                    from math import tan, pi
                    s = int(input())
                    n = int(input())
                    g = (n * s ** 2) / (4 + tan(pi/n))
                    print(g)
                    return g

    def summ():
                    print("Сумма n чисел ")
                    n = int(input())
                    s = (n * (n + 1)) / 2
                    print(s)
                    return s


    if t == 1:
        i = pramoug()
        return i
    if t == 2:
        i = summ()
        return i



cmd = int(input())
vbor(cmd)
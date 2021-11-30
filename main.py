
from datetime import datetime

def timer1 (feuncshn):

    def weper():
        start = datetime.now()
        result = feuncshn ()
        print(datetime.now() - start)
        return result
    return weper

@timer1
def nazv ():
    l = "Вызывается функция"
    return l
@timer1
def f_tecush ():
    n = input()
    return n
K1 = nazv()
K2 = f_tecush()
print(K1)
print(K2)




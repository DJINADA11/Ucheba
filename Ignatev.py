

def tnow():
    '''Текущее время'''
    import datetime
    dt_now = datetime.datetime.now()
    return dt_now

def text():
    word = 'Была вызвана функция: '
    return word

print (text(), tnow.__doc__, tnow())

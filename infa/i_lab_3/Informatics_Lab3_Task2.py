# Author = Koblents Maria Alekseevna
# Group = P3106
# Date = 06.10.2025
print(501832%5) #2
from re import *
def f(x):
    return 5*x**3 -13



def code(s):
    def replace_func(match):
        number = int(match.group(1))
        result = f(number)
        return str(result)
    
    s2 = sub(r'(-?\d+)', replace_func, s)
    print(s2)
    
print('test 1')
code('15 + 22 = 37')
print('test 2')
code('У меня 2 яблока и 3 груши.')
print('test 3')
code('Температура 0 градусов.')
print('test 4')
code("Год основания: 1703.")
print('test 5')
code('Цены: 10 руб., 25 (со скидкой), и 100!')
print('test 6')
code('Привет, мир! Как дела?')
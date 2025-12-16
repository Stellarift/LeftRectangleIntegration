import math

#ввод данных
a = float(input("a = "))
b = float(input("b = "))
eps = float(input("eps = "))

#функция (пример: x^2)
def f(x):
    return x**2

#инициализация
I0 = 0
I1 = float('inf')
n = 5

#основной цикл
while abs(I1 - I0) > eps:
    n = 2 * n
    I0 = I1
    h = (b - a) / n
    I1 = 0
    
    #сумма левых прямоугольников
    for i in range(n):
        x = a + i * h
        I1 = I1 + f(x)
    
    I1 = I1 * h
    
    #Первая итерация
    if I0 == float('inf'):
        I0 = 0

print("I =", I1)
print("n =", n)
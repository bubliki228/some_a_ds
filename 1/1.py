import time
from searchstring import *

def getFibonacciStr(count: int) -> str:  # функция для получения строки из чисел Фибоначчи
    a = ['1', '1']
    if count > 2:
        a = a + [0] * (count - 2)
        for c in range(2, count):
            a[c] = str(int(a[c - 1]) + int(a[c - 2]))
    return "".join(a)

def callSearch(search_function):  # функция для вызова алгоритма поиска и возврата результатов
    global string
    results = [0] * (100 - 10)

    start = time.time()
    for i in range(10, 100):
        results[i - 10] = [i, search_function(str(i), string)]
    timer = time.time() - start

    def by2(res: list):  # функция для сортировки результатов по второму элементу в списке
        return res[1]

    results.sort(key=by2, reverse=True)  # сортировка результатов в обратном порядке
    return (timer, search_function.__name__, results[:3])  # возврат времени выполнения, имени функции и первых трех результатов

if __name__ == "__main__":
    string = getFibonacciStr(500)  # получение строки из 500 чисел Фибоначчи
    print(callSearch(naive))
    print(callSearch(rabinKarp))
    print(callSearch(boyerMoore))

    
    print(callSearch(knuthMorrisPratt))  # вызов функции callSearch с использованием алгоритма Кнута-Морриса-Пратта

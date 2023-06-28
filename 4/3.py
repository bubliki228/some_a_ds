import random

array = [random.randint(1, 100) for i in range(30)] 

max_i = 0  # Максимальная последовательность
cur_i = 0  # Текущая последовательность

for i in range(1, len(array)):
    if array[i] >= array[i - 1]: 
        cur_i += 1

    else:  
        if max_i < cur_i:  # Проверяем, является ли текущая последовательность максимальной
            max_i = cur_i 
        cur_i = 0  

if max_i < cur_i:  # Проверяем, является ли последняя последовательность максимальной
    max_i = cur_i  # Обновляем значение максимальной последовательности

print(max_i) 

from random import randint

N = randint(1, 10)  # количество экспонатов, которые вор хочет украсть
max_weight = randint(1, 30)
treasures = {}

#Словарь с экспонатами
#Ключ - цена экспоната
#Значение - вес


for i in range(randint(1, 20)):  # добавляем экспонаты
    treasures[randint(1, 30)] = randint(1, 30)

print(f"Словарь с экспонатами {treasures}")
print(f"Максимальная грузоподъемность {max_weight}")

count = 0  # счетчик украденных экспонатов
price = 0  # общая цена украденных экспонатов
while count < N:
    current_weight = 0  # текущий вес груза
    while current_weight < max_weight:
        check = False  # флаг для проверки возможности украсть экспонат
        for i in reversed(sorted(treasures.keys())):
            if treasures[i] <= (max_weight - current_weight):
                price += i
                print("Цена и вес украденного: ", i, treasures[i])
                current_weight += treasures[i]
                treasures.pop(i)  # удаляем украденный экспонат из словаря
                check = True  # установка флага, что экспонат был украден
                break
        if not check:
            break  # если не удалось украсть экспонат, выходим из цикла
    count += 1  # увеличиваем счетчик украденных экспонатов

print("Конечная цена: ", price)

from random import randint

cash = {}  # словарь для хранения монет: ключ - цена монеты, значение - количество монет

# Генерация случайных монет
for i in range(4):
    coin = randint(1, 10)  # случайное значение цены монеты
    count = randint(1, 10)  # случайное количество монет данной цены
    while coin in cash.keys():
        coin = randint(1, 10)  # повторная генерация, если монета с такой ценой уже существует
    cash[coin] = count  # добавление монеты в словарь cash

total_cash = 0
for i in cash:  # вычисление общей суммы всех имеющихся монет
    total_cash += i * cash[i]
print(cash)

N = randint(1, total_cash)  # случайная сумма, которую нужно выдать

summ = 0

gived = []  # список выданных монет
while summ < N:
    moneys = list(reversed(sorted(cash.keys())))  # список монет, отсортированный по убыванию цены
    i = 0
    while i < len(moneys):
        if (moneys[i] <= (N - summ)) and cash[moneys[i]] != 0:
            cash[moneys[i]] -= 1  # уменьшение количества доступных монет данной цены
            summ += moneys[i]  # добавление цены монеты к сумме
            gived.append(moneys[i])  # добавление монеты в список выданных монет
            break
        i += 1
    if i == len(moneys):
        for i in reversed(moneys):
            if cash[i] != 0:
                summ += i
                gived.append(i)
                break

print(f"Сумма, которую надо выдать: {N}")
print(f"Выданная сумма: {summ}\nМонеты, которые были выданы: {gived}")

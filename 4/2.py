def multiplyOrder(p):
    n = len(p) - 1  # Количество матриц
    dp = [[0 for i in range(n)] for j in range(n)]  # Инициализация таблицы dp

    for i in range(n):
        dp[i][i] = 0  # Заполняем диагональные элементы нулями

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            dp[i][j] = float('inf')  # Инициализация элемента dp[i][j] бесконечностью
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1])  # Заполнение таблицы dp

    return dp[0][n - 1]  # Возвращаем результат умножения

test = [10, 100, 5, 50]
print(multiplyOrder(test))

board = [['-' for i in range(8)] for j in range(8)]

def board_print(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()

def is_safe(row, column, board):
    # Проверяем столбец на наличие ферзя
    for i in range(row):
        if board[i][column] == 'Q':
            return False

    # Проверяем диагональ, идущую влево и вверх
    i = row
    j = column

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Проверяем диагональ, идущую вправо и вверх
    i = row
    j = column

    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solution(row, board):
    # Если достигли последней строки, то выводим результат
    if row == len(board):
        board_print(board)
        print()
        return

    # Пробуем разместить ферзя в каждой колонке текущей строки
    for i in range(len(board)):
        if is_safe(row, i, board):
            board[row][i] = 'Q'  # Размещаем ферзя
            solution(row + 1, board)  # Рекурсивно вызываем функцию для следующей строки
            board[row][i] = '-'  # Очищаем ячейку после рекурсивного вызова

solution(0, board)

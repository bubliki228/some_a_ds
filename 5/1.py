board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

Xrow = [0, 0, 0]  # Счетчики для рядов с крестиками
Xcolumn = [0, 0, 0]  # Счетчики для колонок с крестиками
Xdiag = [0]  # Счетчик для главной диагонали с крестиками
Xanti_diag = [0]  # Счетчик для побочной диагонали с крестиками

Orow = [0, 0, 0]  # Счетчики для рядов с ноликами
Ocolumn = [0, 0, 0]  # Счетчики для колонок с ноликами
Odiag = [0]  # Счетчик для главной диагонали с ноликами
Oanti_diag = [0]  # Счетчик для побочной диагонали с ноликами

curr_player = 0  # Текущий игрок: 0 - крестики, 1 - нолики


def tablePrinter():
    # Функция для печати текущего состояния игрового поля
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print('\n')
    print('\n')


tablePrinter()


def winCheck(r, c):
    '''
    Функция для проверки наличия выигрышной комбинации после каждого хода

    Крестики - четные числа
    Нолики - нечетные числа
    '''
    if curr_player % 2 == 0:
        Xrow[r] += 1
        Xcolumn[c] += 1
        if r == c:
            Xdiag[0] += 1
        if r + c == 2:
            Xanti_diag[0] += 1

        if Xrow[r] == 3 or Xcolumn[c] == 3 or Xdiag[0] == 3 or Xanti_diag[0] == 3:
            print("Крестики победили")
            return True

    if curr_player % 2 == 1:
        Orow[r] += 1
        Ocolumn[c] += 1
        if r == c:
            Odiag[0] += 1
        if r + c == 2:
            Oanti_diag[0] += 1

        if Orow[r] == 3 or Ocolumn[c] == 3 or Odiag[0] == 3 or Oanti_diag[0] == 3:
            print("Нолики победили")
            return True

    return False


def placer(r, c):
    # Функция для размещения символа текущего игрока на игровом поле
    if curr_player % 2 == 0:
        board[r][c] = 'X'
    else:
        board[r][c] = 'O'


r = int(input("Введите ряд: "))
c = int(input("Введите колонку: "))
placer(r - 1, c - 1)
tablePrinter()

while not winCheck(r - 1, c - 1):
    curr_player += 1
    r = int(input("Введите ряд: "))
    c = int(input("Введите колонку: "))
    placer(r - 1, c - 1)
    tablePrinter()

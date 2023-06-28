def str_key(string):
    code = ''
    for i in string:
        code += str(ord(i))   # Получаем коды символов строки и объединяем их в одну строку
    return int(code)


def bin_str_key(string):
    return ' '.join(format(ord(i), 'b') for i in string)   # Преобразуем символы строки в двоичное представление


def multiplication(key_s):
    hash_s = []
    M = len(key_s)
    C = 0.6180339887   # Константа для умножения
    for i in key_s:
        if type(i) == str:
            key = str_key(i)   # Если элемент строки является строкой, преобразуем его в числовой ключ
            hash_s.append((((key * C) % 1) * M) // 1)   # Вычисляем хеш с использованием умножения
        else:
            hash_s.append((((i * C) % 1) * M) // 1)   # Вычисляем хеш с использованием умножения
    return hash_s


def crc32(data):
    poly = 0xEDB88320   # Полином для вычисления CRC-32
    crc = 0xFFFFFFFF   # Начальное значение CRC
    data_bytes = bytearray(data, 'utf-8')   # Преобразуем данные в байтовый массив
    for byte in data_bytes:
        for bit in range(8):
            if (crc ^ (byte >> bit)) & 0x00000001:
                crc = (crc >> 1) ^ poly   # Вычисляем CRC-32
            else:
                crc = crc >> 1
    return '{:08X}'.format(crc)   # Форматируем CRC-32 в шестнадцатеричное представление
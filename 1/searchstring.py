def naive(pattern_str: str, source_str: str) -> int:    # наивный алгоритм
    pattren_len = len(pattern_str)                      # находим длины подстроки и строки
    source_len = len(source_str)
    found_count = 0

    for l in range(source_len - pattren_len + 1):       # проходимся по всем элементам строки кроме последних pattren_len - 1
        found = True
        for f in range(pattren_len):                    # если какой-то элемент в подстроке не совпал, то идем дальше по строке
            if source_str[l + f] != pattern_str[f]:
                found = False
                break
        if found:                                       # если совпал, то +1
            found_count += 1

    return found_count

def naive_fast(pattern_str: str, source_str: str) -> int:   # наивный алгоритм fast
    pattren_len = len(pattern_str)                      # находим длины подстроки и строки
    source_len = len(source_str)
    found_count = 0

    for l in range(source_len - pattren_len + 1):       # проходимся по всем элементам строки кроме последних pattren_len - 1
        if pattern_str == source_str[l: l + pattren_len]:   # если совпал, то +1
            found_count += 1

    return found_count

def rabinKarp(pattern_str: str, source_str: str) -> int:# алгоритм Рабина-Карпа
    pattern_ind = len(pattern_str) - 1                  # длина шаблона в индексах

    pattern_len = len(pattern_str)                      # длины шаблона и строки
    source_len = len(source_str)

    alphabet_list = []                                  # список с буквами алфавита (добавляем в него буквы)
    for char in pattern_str + source_str:
        if not (char in alphabet_list):
            alphabet_list.append(char)

    alphabet_len = len(alphabet_list)                   # длина алфавита

    def getHash(hash_str: str):                         # получение хэша от шаблона и каждой подстроки
        hash_power = pattern_ind
        hash = 0
        for hs in hash_str:                             # умножается каждый индекс буквы на длину алфавита в степени порядка ее в хэшируемой строке (с конца с 0)
            hash += alphabet_list.index(hs) * alphabet_len ** hash_power
            hash_power -= 1
        return hash
    
    pattern_hash = getHash(pattern_str)                 # хэш шаблона
    found_count = 0                                     # кол-во совпадений
    
    for l in range(source_len - pattern_len + 1):
        source_sub = source_str[l: l + pattern_len]     # срез подстроки длиной шаблона в исходной строке
        sub_hash = getHash(source_sub)                  # хэш подстроки
        if sub_hash == pattern_hash and pattern_str == source_sub:
            found_count += 1                            # увеличиваем счетчик совпадений

    return found_count

def rabinKarp_fast(pattern_str: str, source_str: str) -> int:  # алгоритм Рабина-Карпа
    pattern_ind = len(pattern_str) - 1                  # длина шаблона в индексах

    pattern_len = len(pattern_str)                      # длины шаблона и строки
    source_len = len(source_str)

    alphabet_list = list(set(source_str + pattern_str))               # список с буквами алфавита (добавляем в него буквы)

    alphabet_len = len(alphabet_list)                   # длина алфавита

    def getHash(hash_str: str):                         # получение хэша от шаблона и каждой подстроки
        hash_power = pattern_ind
        hash = 0
        for hs in hash_str:                             # умножается каждый индекс буквы на длину алфавита в степени порядка ее в хэшируемой строке (с конца с 0)
            hash += alphabet_list.index(hs) * alphabet_len ** hash_power
            hash_power -= 1
        return hash
    
    pattern_hash = getHash(pattern_str)                 # хэш шаблона
    found_count = 0                                     # кол-во совпадений
    
    for l in range(source_len - pattern_len + 1):
        source_sub = source_str[l: l + pattern_len]     # срез подстроки длиной шаблона в исходной строке
        sub_hash = getHash(source_sub)                  # хэш подстроки
        if sub_hash == pattern_hash and pattern_str == source_sub:
            found_count += 1                            # увеличиваем счетчик совпадений

    return found_count

def boyerMoore(pattern_str: str, source_str: str) -> int:   # алгоритм Бойера-Мура
    pattern_len = len(pattern_str)                      # длины шаблона и строки
    source_len = len(source_str)

    offset = 0                                          # сдвиг шаблона
    found_count = 0                                     # число совпадений
    l = 0                                               # индекс
    while offset + pattern_len - 1 < source_len:        # пока наше смещение + длина шаблона - 1 не больше длины строки (пока индекс не вышел за строку)
        found = True
        for l in range(pattern_len - 1, -1, -1):        # если какой-то элемент не совпал, то совпадение строк не считаем (идем с конца)
            if source_str[l + offset] != pattern_str[l]:
                found = False
                break

        if found:                                       # иначе - считаем
            found_count += 1
        
        for l in range(pattern_len - 2, -1, -1):        # проходимся по шаблону без последнего элемента (идем с конца)
            found_char = False
            if source_str[offset + pattern_len - 1] == pattern_str[l]:  # если мы находим какую-то букву из этой части шаблона, которая совпадает с буквой в строке, на которой мы остановились
                offset += pattern_len - 1 - l           # то мы находим расстояние от найденной буквы до нее и на него смещаемся
                found_char = True
                break

        if not found_char:                              # если совпадающая буква не нашлась, то сдвигаемся на длину щаблона
            offset += pattern_len
    
    return found_count

def boyerMoore_fast(pattern_str: str, source_str: str) -> int:  # алгоритм Бойера-Мура
    pattern_len = len(pattern_str)                      # длины шаблона и строки
    source_len = len(source_str)

    offset = 0                                          # сдвиг шаблона
    found_count = 0                                     # число совпадений
    l = 0                                               # индекс
    while offset + pattern_len - 1 < source_len:        # пока наше смещение + длина шаблона - 1 не больше длины строки (пока индекс не вышел за строку)
        if pattern_str == source_str[offset: offset + pattern_len]:  # если шаблон равен сдвинутой подстроке, то считаем
            found_count += 1
        
        for l in range(pattern_len - 2, -1, -1):        # проходимся по шаблону без последнего элемента (идем с конца)
            found_char = False
            if source_str[offset + pattern_len - 1] == pattern_str[l]:  # если мы находим какую-то букву из этой части шаблона, которая совпадает с буквой в строке, на которой мы остановились
                offset += pattern_len - 1 - l           # то мы находим расстояние от найденной буквы до нее и на него смещаемся
                found_char = True
                break

        if not found_char:                              # если совпадающая буква не нашлась, то сдвигаемся на длину щаблона
            offset += pattern_len
    
    return found_count

def prefixFunc(pre_str: str) -> int:                    # префикс-функция                  
    pre_len = len(pre_str)                              # длина входной строки
    prefixes = [0] * pre_len                            # массив с нулями, который мы будем заполнять

    i = 1                                               # индекс, отвечающий за суффиксы в слове (изначально наше слово будет иметь длину 2, т. к. у строки длины один нет ни суффиксов, ни преффиксов)
    j = 0                                               # индекс, отвечающий за префиксы

    while i < pre_len:                                  # пока суффикс не вышел за слово
        if pre_str[i] != pre_str[j]:                    # если буква в суффиксе и буква в префиксе не совпали
            if j > 0:                                   # если номер буквы префикса не 1 (индекс больше 0)
                j = prefixes[j-1]                       # то меняем индекс буквы префикса на длину максимального префикса из слова, у которого нет последней буквы текущего слова
            else:                                       # если же буква первая в префиксе, то совпадений нет
                prefixes[i] = 0                         # и слово длиной i + 1 не имеет совпадающих суффиксов и префиксов
                i += 1                                  # увеличиваем суффикс и длину слова
        else:                                           # если же буква префикса и буква суффикса совпали
            prefixes[i] = j + 1                         # то в массив под индекс i записываем номер буквы префикса + 1
            i += 1                                      # увеличиваем индексы суффикса и префикса
            j += 1

    return prefixes

def knuthMorrisPratt(pattern_str: str, source_str: str) -> int: # алгоритм Кнута-Морриса-Прата
    pattern_len = len(pattern_str)                      # длины шаблона и строки
    source_len = len(source_str)
    pattern_prefixes = prefixFunc(pattern_str)          # результаты префикс-функции для шаблона

    found_count = 0                                     # кол-во совпадений
    i = 0                                               # указатели для строки и шаблона
    j = 0

    while i < source_len:                               # пока мы не вышли за строку
        if source_str[i] == pattern_str[j]:             # если у нас совпали буквы в указателях
            i += 1                                      # то мы увеличиваем указатели
            j += 1
            if j == pattern_len:                        # если указатель шаблона равен его длине
                found_count += 1                        # то получается, что мы нашли совпадение, увеличиваем счетчик
                j = pattern_prefixes[j - 1]             # а сам указатель принимает значение от префикс-функции, где слово - весь шаблон (то есть мы сдвигаем на максимальное значение совпадающего суффикса и префикса)
        else:                                           # если буквы не совпали
            if j > 0:                                   # если указатель слова не на первой букве с индексом 0 
                j = pattern_prefixes[j - 1]             # то он принимает значение от результата префикс-функции с длиной совпвдвющего фрагмента
            else:                                       # если указатель нулевой
                i += 1                                  # то мы сдвигаем указатель строки на 1

    return found_count
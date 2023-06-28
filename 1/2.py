from wikidocx import *
from searchstring import knuthMorrisPratt

if __name__ == "__main__":
    referat = getReferatText("Рентгеновское излучение.docx")  # получение текста из файла "Рентгеновское излучение.docx"

    wikipage = getWikipediaText("Рентгеновское излучение")  # получение текста со страницы "Рентгеновское излучение" на Википедии

    referat_list = referat.split()  # разделение текста  на список слов
    referat_len = len(referat) 
    plagiat_syms = 0  # переменная для хранения суммарного количества символов плагиата

    for rl in range(len(referat_list) - 2):  # проход по каждому тройному набору слов в реферате
        search_str = " ".join(referat_list[rl: rl + 3])  # формирование строки для поиска из трех последовательных слов
        count_found = knuthMorrisPratt(search_str, wikipage)  # поиск количества вхождений строки в тексте Википедии
        plagiat_syms += len(search_str) * count_found  # добавление количества символов плагиата к общей сумме

    plagiat = plagiat_syms / referat_len  # вычисление процента плагиата
    print(plagiat)  # вывод процента плагиата

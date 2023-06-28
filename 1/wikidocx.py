import docx
import wikipedia

def getReferatText(file_name: str) -> str: # получение текста из реферата
    referat_file = docx.Document(file_name)
    referat_text = ""
    for paragraph in referat_file.paragraphs:
        referat_text += paragraph.text + "\n"
    return referat_text

def getWikipediaText(page_name: str, set_ru : bool = True) -> str: # получение текста из статьи Википедии
    if set_ru:
        wikipedia.set_lang("ru")
    wiki_page = wikipedia.page(page_name)
    wiki_text = wiki_page.content
    return wiki_text

def notpunctuation(text: str, punctuation: list = [",", ".", "\n", "-", "?", "!"]) -> str: # удаление знаков пунктуации
    for punc in punctuation:
        text_sp = text.split(punc)
        text = "".join(text_sp)
    text = text.lower()
    return text

import pytest
from string_utils import StringUtils

def test_capitilize():
    utils = StringUtils()
    assert utils.capitilize("skypro") == "Skypro"   #делает первую букву заглавной
    assert utils.capitilize("123") == "123"  #при вводе цифр, не делает заглавной, возвращает цифры
def test_trim():
    utils = StringUtils()
    assert utils.trim("   skypro") == "skypro"  #убирает пробелы в начале
    assert utils.trim("sky pro") == "sky pro"   #оставляет пробелы, которые не в начале
def test_to_list():
    utils = StringUtils()
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]     #возвращает список с разделителем по умолчанию
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]   #возвращает список с указанным разделителем
    assert utils.to_list("") == []      #возвращает пустой список при пустом значении
    assert utils.to_list("1,2,3", ":") == ["1,2,3"]     #при неверном разделителе не делает список, возвращает строку
def test_contains():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") == True    #в строке есть искомый символ
    assert utils.contains("SkyPro", "U") == False   #в строке нет искомого символа
    assert utils.contains("", "U") == False     #в пустом значении нет искомого символа
def test_delete_symbol():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"    #искомый символ удален
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"   #удалены несколько искомых символов
    assert utils.delete_symbol("Python Pytest", "P") == "ython ytest"  # удалены несколько искомых символов
    assert utils.delete_symbol("", "m") == ""   #в пустом значении возвращает пустое значение, тк не может найти искомый символ
def test_starts_with():
    utils = StringUtils()
    assert utils.starts_with("SkyPro", "S") == True     #начинается с искомого символа
    assert utils.starts_with("SkyPro", "P") == False    #не начинается с искомого символа
def test_end_with():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "o") == True    #заканчивается искомым символом
    assert utils.end_with("SkyPro", "y") == False   #не заканчивается искомым символом

def test_is_empty():
    utils = StringUtils()
    assert utils.is_empty("") == True    #строка пустая
    assert utils.is_empty(" ") == True      #строка пустая
    assert utils.is_empty("SkyPro") == False    #строка не пустая

def test_list_to_string():
    utils = StringUtils()
    assert utils.list_to_string([1, 2, 3, 4], ", ") == "1, 2, 3, 4"     #список преобразился в строку с правильным разделителем
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"       #список преобразился в строку с правильным разделителем


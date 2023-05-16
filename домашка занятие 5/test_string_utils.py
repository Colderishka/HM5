import pytest
from string_util import StringUtils

#метод capitilize
@pytest.mark.positive_test_capitilize
@pytest.mark.parametrize ( 'line, result', [("привет", "Привет"), ('123', "123"), ("Добрый день", "Добрый день") ])   
def test_positive_capitilize( line, result ):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res == result

@pytest.mark.negative_test_capitilize
@pytest.mark.parametrize ( 'line, result', [ ("", ""),# должен падать но проходит тест
                                             (" ", " "), #также должен падать но проходит
                                             (None, None)                                        
                                             ])
def test_negative_capitilize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res == result
    
#метод trim

@pytest.mark.positive_test_trim
@pytest.mark.parametrize ( 'line, result', [ ("   дом", "дом"), ("крыша", "крыша"), (" 123", "123") ])   
def test_positive_trim( line, result ):
    stringutils = StringUtils()
    res = stringutils.trim(line)
    assert res == result
   
@pytest.mark.negative_test_trim
@pytest.mark.parametrize ( 'line, result', [ ("", ""),# должен падать но проходит тест
                                             (" ", ""), #также должен падать но проходит
                                               (None,None), ])
def test_negative_test_trim(line, result):
    stringutils = StringUtils()
    res = stringutils.trim(line)
    assert res == result

#метод to_list

@pytest.mark.positive_to_list
@pytest.mark.parametrize ( 'line, deli, result ', [ ("a,b,c,d", ",", ["a", "b", "c", "d"] ), 
                                            ("1:2:3", ":", ["1", "2", "3"] ) ] )                                            
def test_positive_to_list( line, result, deli ):
    stringutils = StringUtils()
    res = stringutils.to_list(line, deli)
    assert res == result


@pytest.mark.negative_to_list
@pytest.mark.parametrize ( 'line, deli, result ', [ ("", "", []),# т.к в функции есть метод возвращающий пустой список если аргумента нет то это не ошибка
                                                   (" ", " ", []),#тоже самое
                                                   (None, None, None),
                                                    ])                                         
def test_negative_to_list( line, result, deli ):
    stringutils = StringUtils()
    res = stringutils.to_list(line, deli)
    assert res == result


#метод contains

@pytest.mark.positive_contains
@pytest.mark.parametrize ( 'line, simbol, result', [ ("Привет", "П", True), ("123", "1", True), ]  )                                           
def test_positive_contains( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.contains(line, simbol)
    assert res == result

@pytest.mark.negative_contains
@pytest.mark.parametrize ( 'line, simbol, result', [ ("", "", ValueError), (" ", " ", ValueError), ("Дом", "П", False) ]  )                                            
def test_negative_contains( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.contains(line, simbol)
    assert res == result

#метод delete_symbol

@pytest.mark.positive_delete_symbol
@pytest.mark.parametrize ( 'line, simbol, result', [ ("Привет", "П", "ривет"), ("123", "3", "12") ]  )                                            
def test_positive_delete_symbol( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(line, simbol)
    assert res == result

@pytest.mark.negative_delete_symbol
@pytest.mark.parametrize ( 'line, simbol, result', [ ("", "", ""), (" ", " ", "" ), ("Дом", "П", "Дом") ]  )                                         
def test_delete_symbol( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(line, simbol)
    assert res == result

#метод starts_with
@pytest.mark.positive_starts_with
@pytest.mark.parametrize ( 'line, simbol, result', [ ("Текст", "Т", True), ("123", "1", True), ("14 мая 2023", "1", True) ]  )                                           
def test_positive_starts_with( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.starts_with(line, simbol)
    assert res == result

@pytest.mark.negative_starts_with
@pytest.mark.parametrize ( 'line, simbol, result', [ ("", "", False), (" ", " ", False), ("Пруд", "р", False) ]  )                                            
def test_negative_starts_with( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.starts_with(line, simbol)
    assert res == result

#метод end_with
@pytest.mark.positive_end_with
@pytest.mark.parametrize ( 'line, simbol, result', [ ("Терем", "м", True), ("123", "3", True), ("04 апреля 2024", "4", True) ]  )                                           
def test_positive_end_with( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.end_with(line, simbol)
    assert res == result

@pytest.mark.negative_end_with
@pytest.mark.parametrize ( 'line, simbol, result', [ ("", "", False), (" ", " ", False), (None, None, True), ("tree", "t", False) ]  )                                           
def test_negative_end_with( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.end_with(line, simbol)
    assert res == result

#метод is_empty

@pytest.mark.positive_is_empty
@pytest.mark.parametrize ( 'line, result', [ ("", True), (" ", True) ]  )                                           
def test_positive_is_empty( line, result ):
    stringutils = StringUtils()
    res = stringutils.is_empty(line,)
    assert res == result

@pytest.mark.negative_is_empty
@pytest.mark.parametrize ( 'line, result', [ ("123", False), ("Дом", False), (",,", False) ]  )                                           
def test_negative_is_empty( line, result ):
    stringutils = StringUtils()
    res = stringutils.is_empty(line,)
    assert res == result

#метод list_to_string

@pytest.mark.positive_list_to_string
@pytest.mark.parametrize ( 'line, simbol, result', [ ([1, 2, 3, 4], ",", "1,2,3,4" ), (["Солн", "це"], ":", "Солн:це") ]  )                                            
def test_positive_list_to_string( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.list_to_string(line, simbol)
    assert res == result

@pytest.mark.negative_list_to_string
@pytest.mark.parametrize ( 'line, simbol, result', [ ([],",", ""),
                                                     ([" "], ",", " "),
                                                       (None, ",", None)
                                                       #т.к условия первых двух теста прописаны в методе то это не баги 
                                                         ] )                                            
def test_negative_list_to_string( line, simbol, result ):
    stringutils = StringUtils()
    res = stringutils.list_to_string(line, simbol)
    assert res == result

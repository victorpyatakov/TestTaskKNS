"""
Тестовое задание ООО КНС ГРУПП
Пятаков В. С.
30.01.2021
"""
class BracketAnalyze():
    """
    Класс для анализа количества открывающих и закрывающих скобок в строке
    """
    def __init__(self, string_with_brackets:str):
        self.__string_with_brackets = string_with_brackets


    def __get_dict_brakets(self) -> dict:
        """
        Метод для получения словаря скобок.
        """
        return {
                    ')' : '(',
                    ']' : '[',
                    '}' : '{'
        }           


    def is_count_brackets_equal(self) -> bool:
        """
        Метод для определния количества и правильного следования скобок.
        """
        dict_brackets = self.__get_dict_brakets()
        list_brackets = []
        for char in self.__string_with_brackets:
            if char in dict_brackets.values():
                    list_brackets.append(char)
                    continue
            if char in dict_brackets:
                if dict_brackets[char] in list_brackets:
                    list_brackets.pop()
                    continue
                else:
                    return False
        if len(list_brackets) > 0:
            return False
        else:
            return True



if __name__ == "__main__":
    test_string = '((({([{[ }])})))'
    brackets_analiser = BracketAnalyze(test_string)
    result = brackets_analiser.is_count_brackets_equal()
    print(result)
    

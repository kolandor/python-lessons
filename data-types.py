#################Типы данных в Python#################

isMaried = False
print(isMaried)

isAvalible = True
print(isAvalible)

myAge = 32
print(myAge)

binaryNumber = 0b1000001 #двоичное число записывается так
print(binaryNumber)

octNumber = 0o11 #восьмиричное число записывается так
print(octNumber)

hexNumber = 0xF #шеснадцатиричные число записывается так
print(hexNumber)

#простыми словами комплексное число просто хранит два числа сразу, применить можно например для координат
complexNumber = 2 + 3j #комплексные числа записываются так, j помечает мнимую часть
print(complexNumber)

stringSampleDual = "Hello, World!" #пример написани строки две кавычки
stringSampleSingle = 'Hello, World!' #пример написани строки одна
# можно и так и так, но в каких случаяях одно лучше другого
strExamle = "'Hello'" # мне не пришлось экранировать кавычку, то есть писать \'
print(strExamle)
strExamle = '"Hello"' # мне не пришлось экранировать кавычку, то есть писать \"
print(strExamle)

#Многострочные строки
multiLineStr = ("Привет!\n" #Я тут явно указал символ переноса строки
                "Как дела?")
print(multiLineStr)

#Вот пример многострочной строки с поддрежкой переноса строк
text = '''
А вот тут уже можно писать
текст как я хочу

И сколько хочу'''
print(text)

"""
Эта же строка может быть написана с использованием двойных кавычек
А также в пайтоне её используют как многострочный комментарий не привязывая её к переменной
"""

#Пример проблемы с обратными слешами в строках
path = "C:\python\name.txt"
print(path)

#Решение проблемы с обратными слешами в строках
path = r"C:\python\name.txt"
print(path)
#Тут я использовал сырую (RAW SRING) строку, которая игнорирует все спец символы, в том числе и \n, \t и т.д.

#Многострочная строка с поддержкой переноса строк и без проблем с обратными слешами
text = r'''What is the best regular expression to check if a string is a valid URL?
Asked 17 years, 6 months ago
Modified 5 months ago
Viewed 776k times
1094
\b(?:(?:[A-Za-z][A-Za-z0-9+.\-]*):\/\/)?(?:www\.)?[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}(?:\/\S*)?(?=\s|$) or "\\b(?:(?:[A-Za-z][A-Za-z0-9+.\\-]*):\\/\\/)?(?:www\\.)?[A-Za-z0-9\\-]+(?:\\.[A-Za-z0-9\\-]+)*\\.[A-Za-z]{2,}(?:\\/\\S*)?(?=\\s|$)" – 
Sathvik
 CommentedMay 8, 2025 at 19:38'''
print(text)

#Форматирование строк (интерполяция строк)
name = "Alice"
#Использование f-строк для форматирования с примером вызова функции внутри строки
formattedString = f"My name is {name} and I am {input('How old are you: ')} years old."
print(formattedString)
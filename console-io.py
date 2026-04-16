# Пример использования параметров sep и end в функции print
name1 = "Igor"
name2 = "Evgenia"
name3 = "Vchera progulyala"

print(f"PARAM1 = {name1}", f"PARAM2 = {name2}", f"PARAM3 = {name3}", sep=" sep ", end=" end\n")

#format - старый способ форматирования строк, который позволяет вставлять значения в строку с помощью фигурных скобок {} и метода format()
print("Ne progilival: {}, {}".format(name1, name2))

#Открываем файл MyData.txt в режиме записи ("w" - write). Если файла нет, он будет создан. Если файл уже существует, его содержимое будет перезаписано.
with open("MyData.txt", "w") as myFileData:
    #Параметр file=myFileData указывает, что вывод функции print должен быть направлен в файл myFileData вместо стандартного вывода (консоли). В данном случае, строка "Ne progilival: Igor, Evgenia" будет записана в файл MyData.txt.
    print("Ne progilival: {}, {}".format(name1, name2), file=myFileData) 

# Пример использования параметров end и flush в функции print
'''import time

for i in range(5):
    print(i, end=" ", flush=True) #flush=True - принудительно очищает буфер вывода после каждого print
    time.sleep(1)'''

 #Функция input() позволяет пользователю ввести данные с клавиатуры. В данном случае, она запрашивает у пользователя ввести его имя. После ввода и нажатия Enter, введенное значение будет возвращено функцией input() и может быть сохранено в переменной или использовано в дальнейшем коде.
name = input("Input your name: ")
print(f"Hello, {name}!")

try:
    age = int(input("Input your age: "))
    print(f"Your age is: {age}")
except:
    print("NOT A NUMBER, YOU ARE FUCKING IDIOT!")

print("Program is finished")
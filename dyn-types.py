#################Динамические типы данных в Python#################
userId = 12345 #Переменная userId хранит целое число (тип данных int)
print("userId:", userId, "\nType:", type(userId))

userId = "ALEX" #Теперь переменная userId хранит строку (тип данных str)
print("\nuserId:", userId, "\nType:", type(userId))

# Пример использования преобразования типа данных
userAge = input("\nВведите ваш возраст: ") #input всегда возвращает строку (тип данных str)
print("\nuserAge:", userAge, "\nType:", type(userAge))

userAge = int(userAge) #Преобразуем строку в целое число (тип данных int)
print("\nuserAge:", userAge, "\nType:", type(userAge)) 

#или можно было сразу так
userAge = int(input("\nВведите ваш возраст: ")) #Преобразуем строку в целое число (тип данных int) сразу при вводе
print("\nuserAge:", userAge, "\nType:", type(userAge))
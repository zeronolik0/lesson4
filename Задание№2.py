# Запрос пятизначного числа от пользователя
print("Введите пятизначное число")
number = int(input())

# Преобразование числа в строку 
num_str = str(number)

# Извлечение нужных цифр:
# Десятки тысяч - первая цифра
tenthousands = int(num_str[0])
# Тысячи - вторая цифра
thousands = int(num_str[1])
# Сотни - третья цифра
hundreds = int(num_str[2])
# Десятки - четвёртая цифра
tens = int(num_str[3])
# Единицы - пятая цифра
ones = int(num_str[4])

# Возводим количество десятков в степень количества единиц
power_result = tens ** ones

# Умножаем результат на количество сотен
multiplied = power_result * hundreds

# Вычисляем делитель: разница между десятками тысяч и тысяч
denominator = tenthousands - thousands

# Выполняем деление, учитывая возможность деления на ноль
if denominator != 0:
    result = multiplied / denominator
else:
    result = float('inf')  
print(result)
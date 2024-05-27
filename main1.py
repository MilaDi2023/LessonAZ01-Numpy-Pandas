import pandas as pd


# СПОСОБ 1. СОЗДАНИЕ SERIES
data =[1, 2, 3, 4, 5] # Создаём список
series = pd.Series(data) # Пересохраняем список в другую переменную
print(series) # Вывод индексированного списка в виде одномерного массива

# СПОСОБ 2. СОЗДАНИЕ DATA FRAME
# Сначала созадём словарь
data = {
    "Name" : ["Alice", "Bob", "Roma", "Anna"],
    "Age": [23, 45, 17, 24],
    "City": ["New York", "Los Angeles", "Chicago", "Moscow"]
}

# Затем преобразовываем его в таблицу
df = pd.DataFrame(data)
print(df) # Выводим данные в виде таблицы

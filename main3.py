# Функции редактирования и анализа датафрейма на примере дата-сета hh.csv

import pandas as pd

df = pd.read_csv("hh.csv")

# Добавление столбца с заголовком Test и заполнение его значениями от 0 до 28 (по числу записей в дата-сете 29)
# Значения добавляем не вручную, а генерим с помощью цикла
df["Test"] = [new for new in range(29)]

print(df)

# Удаление столбца Test
df.drop("Test", axis=1, inplace=True) # Если axis=0, то удаляется указанная СТРОКА
print(df)

# Удаление строки по её индексу, н-р, удалим последнюю строку с индексом 28
df.drop(28, axis=0, inplace=True)
print(df)
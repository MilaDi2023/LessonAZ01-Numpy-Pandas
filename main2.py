# РАБОТА С ДАТА СЕТОМ World-hapiness-report-2024.csv

import pandas as pd

# Считываем инфу из CSV-файла
df = pd.read_csv("World-happiness-report-2024.csv")

# Смотрим, что хранится в файле (выводятся только первые 5 строк)
print(df.head())

# Смотрим, что хранится в файле (выводятся только последние 5 строк)
print(df.tail())

# Смотрим базовую инфу о дата фрейме (в т.ч. заголовки столбцов и типы данных в них)
print(df.info())

# Смотрим статистическое описание данных
print(df.describe())

# ===========================================================

# Вывод только одного столбца, н-р, столбца со странами
print(df["Country name"])

# Вывод двух столбцов (NB: внимание на синтаксис! Двойные скобки [[...]] )
print(df[["Country name", "Regional indicator"]])

# Вывод всей строки по индексу
print(df.loc[71])

# Вывод не всей строки по индексу, а с выборочными столбцами. Н-р, с двумя
print(f"\n===")
print(df.loc[78, ["Country name", "Generosity"]])

# Вывод инфы по определенному условию, н-р, Healthy life expectancy > 0.7
print(f"\n===")
print(df[df["Healthy life expectancy"] > 0.7])

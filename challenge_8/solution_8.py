import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# генерируем данные
books = ["Программирование на Java", "Rust для профессионалов", "JavaScript для начинающих", "Веб-разработка на Django", "Фронтенд на React"]
regions = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]
platforms = ["BooksOnline", "eBooks", "iSales"]
index = pd.MultiIndex.from_product([books, regions, platforms], names=["Название учебника", "Регион продажи", "Платформа продажи"])
sales_data = np.random.randint(500, 1500, size=(len(index), 1))
prices = np.random.randint(700, 1000, size=(len(index), 1))
total_sales = sales_data * prices
sales_df = pd.DataFrame(np.concatenate((sales_data, prices, total_sales), axis=1),
                        index=index,
                        columns=["Количество проданных книг", "Цена экземпляра", "Объем продаж"])

# настройки для вывода таблиц без сокращений
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# создаем сводную таблицу продаж по регионам и платформам
sales_by_region_platform = sales_df.pivot_table(values='Объем продаж', index='Регион продажи', columns='Платформа продажи', aggfunc=np.sum)
print(f"\nПродажи по регионам и платформам: \n{sales_by_region_platform}")

# создаем сводную таблицу продаж по платформам
sales_by_book_platform = sales_df.pivot_table(values='Объем продаж', index='Название учебника', columns='Платформа продажи', aggfunc=np.sum)
print(f"\nПродажи учебников по платформам: \n{sales_by_book_platform}")

# создаем сводную таблицу продаж по регионам
sales_by_book_region = sales_df.pivot_table(values='Объем продаж', index='Название учебника', columns='Регион продажи', aggfunc=np.sum)
print(f"\nСводная таблица по продажам по книгам и регионам: \n{}")

# визуализируем продажи по регионам
sales_by_book_region.plot(kind='barh', figsize=(10, 6))
plt.title('Продажи книг по регионам')
plt.xlabel('Объем продаж')
plt.ylabel('Название учебника')
plt.show()

# визуализируем продажи по регионам и платформам
sales_by_region_platform.plot(kind='bar')
plt.title('Продажи по регионам и платформам')
plt.xlabel('Регион продажи')
plt.ylabel('Объем продаж')
plt.show()

# визуализируем вклад каждой книги в суммарные продажи
total_sales_by_book = sales_by_book_platform.sum(axis=1)
total_sales_by_book.plot(kind='pie', figsize=(10, 6), autopct='%1.1f%%')
plt.title('Вклад каждой книги в суммарные продажи по регионам и платформам')
plt.ylabel('')
plt.axis('equal')
plt.show()
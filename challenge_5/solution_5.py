import pandas as pd

# oткрываем файл CSV
df = pd.read_csv('movies.csv')
# сохраняем DataFrame в файл XLSX
df.to_excel('movies.xlsx', index=False)
# загружаем данные о фильмах из XLSX файла
data = pd.read_excel('movies.xlsx')

# выводим первые 5 записей
print(f"Первые 5 записей: {data.head()}")

# посчитываем общее количество фильмов
print(f"\nОбщее количество фильмов: {len(data)}")

# посчитываем количество фильмов в каждом жанре
genre_counts = data['Жанр'].value_counts()
print(f"\nКоличество фильмов по жанрам: {genre_counts.to_string(name=False)}")

# определяем фильм с наибольшим рейтингом
max_rating = data['Рейтинг'].max()
best_movie = data[data['Рейтинг'] == max_rating]['Название'].values[0]
print(f"\nФильм с наивысшим рейтингом: {best_movie}")

# вычисляем средний рейтинг фильмов
average_rating = data['Рейтинг'].mean().round(2)
print(f"\nСредний рейтинг фильмов: {average_rating}")

# находим фильмы, выпущенные после 2005 года
movies_after_2000 = data[data['Год'] > 2005]
print(f"\nФильмы, выпущенные после 2005 года: {movies_after_2000}")



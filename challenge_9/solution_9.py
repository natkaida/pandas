import requests
from bs4 import BeautifulSoup
import pandas as pd

# скрапим данные
url = "https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# парсим данные
table = soup.find("table", class_="sortable")
data = []

for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    position = cells[0].text.strip()
    title_cell = cells[1]
    title_link = title_cell.find("a")
    title = title_link.text.strip() if title_link else title_cell.text.strip()
    year = cells[2].text.strip()
    director = cells[3].text.strip()
    genre = cells[4].text.strip()
    url = "https://ru.wikipedia.org" + title_link["href"] if title_link else ""
    data.append([position, title, year, director, genre, url])

df = pd.DataFrame(data, columns=["Место", "Название", "Год", "Режиссер", "Жанр", "URL"])

# преобразуем столбец "Год" в числовой формат
df["Год"] = pd.to_numeric(df["Год"])

# определяем режиссеров, снявших более одного фильма
directors_counts = df["Режиссер"].value_counts()
multiple_director_films = directors_counts[directors_counts > 1]

print("Режиссеры, снявшие более одного фильма из списка:")
for director, count in multiple_director_films.items():
    films = df[df["Режиссер"] == director]
    films_info = films[["Название", "Год"]]
    print(f"\nРежиссер: {director}, количество фильмов: {count}")
    print(films_info)

# выбираем 5 самых новых фильмов
newest_films = df.sort_values("Год", ascending=False).head(5)
print("\nСамые новые фильмы:")
print(newest_films[["Название", "Год", "Режиссер"]].to_string(index=False))

# выбираем 5 самых старых фильмов
newest_films = df.sort_values("Год", ascending=False).tail(5)
print("\nСамые старые фильмы:")
print(newest_films[["Название", "Год", "Режиссер"]].to_string(index=False))

# анализируем жанры
most_common_genre = df["Жанр"].value_counts().idxmax()
print("\nСамый популярный жанр среди высокорейтинговых фильмов:", most_common_genre)

# находим самый старый фильм
oldest_film = df.sort_values("Год").iloc[0]
oldest_year = oldest_film["Год"]
oldest_film_title = oldest_film["Название"]

# создаем временные периоды, начиная с самого старого фильма
start_year = oldest_year
end_year = df["Год"].max()
interval = 7
periods = range(start_year, end_year, interval)

# подсчитываем количество фильмов в каждом периоде
films_per_period = {}
for period in periods:
    period_start = period
    period_end = period + interval - 1
    period_films = df[(df["Год"] >= period_start) & (df["Год"] <= period_end)]
    films_per_period[f"{period_start}-{period_end}"] = len(period_films)

# определяем период с наибольшим количеством фильмов
most_films_period = max(films_per_period, key=films_per_period.get)
films_count = films_per_period[most_films_period]

print("\nПериоды, в которые выходили лучшие фильмы:")
for period, count in films_per_period.items():
    print(f"{period}: {count} фильмов")
print("\nВ периоде", most_films_period, "было снято наибольшее количество фильмов:", films_count)

# сохраняем DataFrame в Excel файл
filename = "top250_films.xlsx"
sheet_name = "топ-250"

with pd.ExcelWriter(filename) as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"\nDataFrame сохранен в файл {filename} на листе {sheet_name}.")

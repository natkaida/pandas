import pandas as pd

# загружаем данные из файла CSV
data = pd.read_csv('sales_data.csv')
month_names = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь'
}

# преобразуем столбец 'Дата' в datetime
data['Дата'] = pd.to_datetime(data['Дата'])

# вычисляем прибыль
data['Прибыль'] = data['Количество'] * data['Цена']

# находим самый прибыльный магазин
profit_by_store = data.groupby('Магазин')['Прибыль'].sum()
most_profitable_store = profit_by_store.idxmax()

# определяем самые популярные фрукты
popular_fruit = data.groupby('Фрукт')['Количество'].sum().idxmax()

# находим самый прибыльный месяц
data['Месяц'] = data['Дата'].dt.month
profit_by_month = data.groupby('Месяц')['Прибыль'].sum()
most_profitable_month = profit_by_month.idxmax()

print(f"Самый прибыльный магазин: {most_profitable_store}")
print(f"Самые популярные фрукты: {popular_fruit.lower()}")
print(f"Самый прибыльный месяц: {month_names.get(most_profitable_month)}")

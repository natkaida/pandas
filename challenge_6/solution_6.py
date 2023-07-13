import pandas as pd
import random

# данныe о продажах
data = {
    'Дата': pd.date_range(start='2023-01-01', end='2023-12-31'),
    'Ноутбуки': [random.randint(250, 5000) for _ in range(365)],
    'Планшеты': [random.randint(550, 9000) for _ in range(365)],
    'Смартфоны': [random.randint(1200, 15000) for _ in range(365)]
}

df = pd.DataFrame(data)

# преобразуем столбец 'Дата' в индекс
df.set_index('Дата', inplace=True)

# вычисляем максимальные и минимальные продажи за каждый месяц
sales_by_month = df.resample('M').agg(['max', 'min'])

# определяем самый успешный и самый неуспешный месяцы
most_successful_month = sales_by_month.idxmax()
least_successful_month = sales_by_month.idxmin()

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

print(f"Максимальные и минимальные продажи за каждый месяц: {sales_by_month}")

print("\nСамый прибыльный месяц по продажам:")
for product in df.columns:
    month_number = most_successful_month.loc[product, 'max'].month
    month_name = month_names.get(month_number)
    print(f"{product} - {month_name}")

print("\nСамый неуспешный месяц по продажам:")
for product in df.columns:
    month_number = least_successful_month.loc[product, 'min'].month
    month_name = month_names.get(month_number)
    print(f"{product} - {month_name}")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# генерируем данные о потреблении электроэнергии за 3 месяца
start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 8, 31)
num_days = (end_date - start_date).days + 1

apartments = [f'Кв. {i}' for i in range(1, 26)]
num_apartments = len(apartments)

data = {
    'Дата и время': [],
    'Квартира': [],
    'Потребление': []
}

for i in range(num_days):
    current_date = start_date + timedelta(days=i)
    for j in range(num_apartments):
        consumption = np.random.randint(4, 15)
        data['Дата и время'].append(current_date)
        data['Квартира'].append(apartments[j])
        data['Потребление'].append(consumption)

df = pd.DataFrame(data)

# изменяем некоторые данные по потреблению на необычно низкие или высокие
num_modifications = np.random.randint(2, 7) 
indices_to_modify = np.random.choice(df.index, size=num_modifications, replace=False)
df.loc[indices_to_modify, 'Потребление'] = np.random.choice([np.random.randint(1, 3), np.random.randint(16, 20)], size=num_modifications)

# добавляем столбец 'Рабочий день' для определения рабочих и нерабочих дней
df['День'] = df['Дата и время'].dt.dayofweek < 5

# вычисляем общее потребление электроэнергии для каждой квартиры за весь период времени
total_consumption = df.groupby('Квартира')['Потребление'].sum()
print(f"Общее потребление электроэнергии по квартирам за 3 месяца:\n {total_consumption.to_string(name=False)}\n")

# находим среднее потребление электроэнергии по каждому месяцу
monthly_mean_consumption = df.resample('M', on='Дата и время')['Потребление'].mean()
monthly_mean_consumption.index.freq = None
print(f"Среднее потребление электроэнергии в месяц:\n {monthly_mean_consumption.to_string(name=False)}\n")

# определяем квартиры с наибольшим и наименьшим потреблением электроэнергии
print(f"Квартира с максимальным потреблением: {total_consumption.idxmax()}")
print(f"Квартира с минимальным потреблением: {total_consumption.idxmin()}")

# находим дни с повышенным потреблением электроэнергии
high_consumption_days = df[df['Потребление'] > df.groupby('Дата и время')['Потребление'].transform('mean') + 2 * df.groupby('Дата и время')['Потребление'].transform('std')]['Дата и время'].dt.date.unique()
print(f"\nДни с повышенным потреблением электроэнергии: {high_consumption_days}")

# определяем среднее потребление электроэнергии для каждой квартиры в рабочие и нерабочие дни
day_type_labels = {True: 'Рабочий', False: 'Выходной'}

# Определяем среднее потребление электроэнергии для каждой квартиры в рабочие и нерабочие дни
mean_consumption_by_day_type = df.groupby(['Квартира', 'День'])['Потребление'].mean()
mean_consumption_by_day_type = mean_consumption_by_day_type.reset_index()
mean_consumption_by_day_type['День'] = mean_consumption_by_day_type['День'].map(day_type_labels)

print(f"\nСреднее потребление по рабочим и выходным дням:\n{mean_consumption_by_day_type}")

# опеределяем квартиры с необычно низким / высоким потреблением
low_threshold = 3
high_threshold = 16

anomaly_apartments = df[df['Квартира'].isin(df.groupby('Квартира')['Потребление'].quantile([0.01, 0.99]).unstack().sum(axis=1).index) & ((df['Потребление'] <= low_threshold) | (df['Потребление'] >= high_threshold))]

print(f"\nКвартиры с необычно низким/высоким потреблением электроэнергии:\n{anomaly_apartments[['Дата и время', 'Квартира', 'Потребление']]}")

# определяем дни с наибольшим и наименьшим потреблением электроэнергии в рабочие и нерабочие дни
max_consumption_working_day = df[df['День']]['Дата и время'].dt.date[df[df['День']]['Потребление'].idxmax()]
min_consumption_working_day = df[df['День']]['Дата и время'].dt.date[df[df['День']]['Потребление'].idxmin()]
max_consumption_non_working_day = df[~df['День']]['Дата и время'].dt.date[df[~df['День']]['Потребление'].idxmax()]
min_consumption_non_working_day = df[~df['День']]['Дата и время'].dt.date[df[~df['День']]['Потребление'].idxmin()]
print(f"\nРабочие дни с наивысшим потреблением: {max_consumption_working_day}")
print(f"Рабочие дни с наименьшим потреблением: {min_consumption_working_day}")
print(f"Выходные дни с наивысшим потреблением: {max_consumption_non_working_day}")
print(f"Выходные дни с наименьшим потреблением: {min_consumption_non_working_day}\n")

# подсчитываем среднее потребление электроэнергии для каждой квартиры
mean_consumption_per_apartment = df.groupby('Квартира')['Потребление'].mean()

# визуализируем среднее потребление электроэнергии по квартирам в виде круговой диаграммы
plt.pie(mean_consumption_per_apartment, labels=mean_consumption_per_apartment.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Среднее потребление электроэнергии по квартирам')
plt.show()
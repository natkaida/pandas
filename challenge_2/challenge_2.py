import pandas as pd

# загружаем данные из файла CSV
data = pd.read_csv('students.csv')

# вычисляем средний балл каждого студента
data['Средний балл'] = data[['Математика', 'Физика', 'Химия', 'Информатика', 'История']].mean(axis=1).round(2)

# установливаем параметры для отображения всех столбцов без сокращения
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# сортируем список по среднему баллу в порядке убывания
sorted_data = data.sort_values(by='Средний балл', ascending=False)
print(sorted_data)

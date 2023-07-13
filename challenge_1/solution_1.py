import pandas as pd
import random

departments = ['Отдел продаж', 'Отдел разработки', 'Отдел маркетинга', 'Отдел финансов']
male_names = ['Павел', 'Егор', 'Иван', 'Сергей', 'Олег', 'Алексей', 'Дмитрий', 'Артем', 'Александр', 'Максим', 'Кирилл', 'Никита']
female_names = ['Мария', 'Анна', 'Марина', 'Екатерина', 'София', 'Александра', 'Елена', 'Ольга', 'Полина', 'Юлия', 'Светлана', 'Анастасия']
male_surnames = ['Иванов', 'Петров', 'Сидоров', 'Ефремов', 'Николаев', 'Смирнов', 'Кузнецов', 'Морозов', 'Егоров']
female_surnames = ['Иванова', 'Петрова', 'Сидорова', 'Ефремова', 'Николаева', 'Смирнова', 'Егорова', 'Кузнецова', 'Морозова']
positions = ['Менеджер', 'Разработчик', 'Маркетолог', 'Финансовый аналитик']

# генерируем данные о сотрудниках
employees = []
names_used = set()
surnames_used = set()

while len(employees) < 36:
    if random.choice([True, False]):
        names = male_names
        surnames = male_surnames
    else:
        names = female_names
        surnames = female_surnames

    department = random.choice(departments)
    position = random.choice(positions)
    salary = random.randint(90000, 280000)

    # проверка на уникальное имя и фамилию
    name = random.choice(names)
    surname = random.choice(surnames)
    if (name, surname) in names_used and surname in surnames_used:
        continue

    names_used.add((name, surname))
    surnames_used.add(surname)

    employees.append([name, surname, department, position, salary])

# создаем и выводим DataFrame с данными о сотрудниках
data = pd.DataFrame(employees, columns=['Имя', 'Фамилия', 'Отдел', 'Должность', 'Зарплата'])
print(data)
min_salary = data['Зарплата'].min()
print("Минимальная зарплата:", min_salary)
max_salary = data['Зарплата'].max()
print("Максимальная зарплата:", max_salary)

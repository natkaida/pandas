import pandas as pd

data = pd.read_csv("weather.csv")

# преобразуем столбцы с числовыми значениями в числовой тип данных
numeric_columns = ["MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine", "WindGustSpeed", "WindSpeed9am", "WindSpeed3pm", "Humidity9am", "Humidity3pm", "Pressure9am", "Pressure3pm", "Cloud9am", "Cloud3pm", "Temp9am", "Temp3pm", "RISK_MM"]
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors="coerce")

# создаем Series из 10 самых теплых дней
hottest_days = data.nlargest(10, "MaxTemp")["MaxTemp"]
hottest_days.index = data.nlargest(10, "MaxTemp")["Date"]
hottest_days.index.name = "Дата"

# создаем Series из 10 самых холодных дней
coldest_days = data.nsmallest(10, "MinTemp")["MinTemp"]
coldest_days.index = data.nsmallest(10, "MinTemp")["Date"]
coldest_days.index.name = "Дата"

# создаем Series из 10 самых ветреных дней
windiest_days = data.nlargest(10, "WindGustSpeed")["WindGustSpeed"]
windiest_days.index = data.nlargest(10, "WindGustSpeed")["Date"]
windiest_days.index.name = "Дата"

# создаем Series из 10 самых засушливых дней
driest_days = data[["Humidity9am", "Humidity3pm"]].nsmallest(10, ["Humidity9am", "Humidity3pm"]).max(axis=1)
driest_days.index = data.nsmallest(10, ["Humidity9am", "Humidity3pm"])["Date"]
driest_days.index.name = "Дата"

# создаем Series из 10 самых ясных дней
clearest_days = data[["Cloud9am", "Cloud3pm"]].nsmallest(10, ["Cloud9am", "Cloud3pm"]).max(axis=1)
clearest_days.index = data.nsmallest(10, ["Cloud9am", "Cloud3pm"])["Date"]
clearest_days.index.name = "Дата"

# проверяем точность прогноза на дождь
results = []
for i in range(len(data) - 1):
    if data.at[i, "RainTomorrow"] == "No" and data.at[i + 1, "RainToday"] == "Yes":
        results.append(data.at[i + 1, "Date"])
    elif data.at[i, "RainTomorrow"] == "Yes":
        if data.at[i + 1, "RainToday"] == "Yes":
            continue
        elif data.at[i + 1, "RainToday"] == "No":
            results.append(data.at[i + 1, "Date"])

print(f"10 самых жарких дней:\n {hottest_days.to_string(name=False)}")
print(f"\n10 самых холодных дней:\n {coldest_days.to_string(name=False)}")
print(f"\n10 самых ветреных дней:\n {windiest_days.to_string(name=False)}")
print(f"\n10 самых влажных дней:\n {driest_days.to_string(name=False)}")
print(f"\n10 самых облачных дней:\n {clearest_days.to_string(name=False)}")
print("\nОшибочные прогнозы на дождь:")
for result in results:
    print(result)

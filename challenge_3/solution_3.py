import pandas as pd

# ежемесячные доходы от инвестиций за 5 лет
investments = pd.Series([100000, 120000, 150000, 80000, 200000, 250000, 180000, 300000, 280000, 320000, 350000, 400000,
                         180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000,
                         150000, 300000, 250000, 280000, 320000, 350000, 380000, 400000, 420000, 440000, 470000, 500000,
                         200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000, 420000,
                         150000, 160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000],
                        index=pd.date_range(start='2019-01-01', periods=60, freq='M'))

# вычисляем годовую доходность
annual_returns = investments.groupby(investments.index.year).sum()

# вычисляем среднюю ежемесячную доходность по каждому году
monthly_returns = investments.groupby(investments.index.year).mean()

print("Годовая доходность:")
print(annual_returns.to_string(name=False))
print("\nСредняя ежемесячная доходность по каждому году:")
print(monthly_returns.round(2).to_string(name=False))
print(f"\nГод с наибольшей доходностью: {annual_returns.idxmax()}")
print(f"Год с наименьшей доходностью: {annual_returns.idxmin()}")

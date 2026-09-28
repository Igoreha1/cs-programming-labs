destination = float(input("Введите расстояние: "))
razhod = float(input("Введите расход топлива: "))
price = float(input("Введите цену топлива: "))

fuel = destination * razhod / 100
cost = fuel * price

print(f"Топливо: {fuel:.2f} л")
print(f"Стоимость: {cost:.2f} руб")
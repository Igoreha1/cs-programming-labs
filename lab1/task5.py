destination = float(input())
razhod = float(input())
price = float(input())

fuel = destination * razhod / 100
cost = fuel * price

print(f"Топливо: {fuel:.2f} л")
print(f"Стоимость: {cost:.2f} руб")
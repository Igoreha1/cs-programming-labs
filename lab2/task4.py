record = input()

train, from_city, to_city, time, price = record.split(";")

print(f"Поезд: {train}")
print(f"Маршрут: {from_city} - {to_city}")
print(f"Отправление: {time}")
print(f"Цена: {float(price):.2f} руб")
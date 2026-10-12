code = input()

category = code[0:3]
year = code[4:8]
number = code[9:13]
reverse_number = number[::-1]

print(f"Категория: {category}")
print(f"Год: {year}")
print(f"Номер: {number}")
print(f"Обратный номер: {reverse_number}")
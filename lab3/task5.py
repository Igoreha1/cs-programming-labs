identifier = input()

length = len(identifier)
only_letters = identifier.isalpha()
only_digits = identifier.isdigit()
alphanumeric = identifier.isalnum()
has_hyphen = "-" in identifier

print(f"Длина: {length}")
print(f"Только буквы: {only_letters}")
print(f"Только цифры: {only_digits}")
print(f"Буквенно-цифровая: {alphanumeric}")
print(f"Содержит дефис: {has_hyphen}")
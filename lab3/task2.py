full_name = input()

surname, name, patronymic = full_name.split()

print(f"{surname.capitalize()} {name[0].upper()}. {patronymic[0].upper()}.")
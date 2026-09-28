sum_seconds = int(input("Введите количество секунд: "))

hours = sum_seconds // 3600
minutes = (sum_seconds % 3600) // 60
seconds = sum_seconds % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
def sum_digits(number):
    number = abs(number)
    if number == 0:
        return 0
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total

def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    return " ".join(text.split()).lower()

def select_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]


num = int(input("Введите целое число (для суммы цифр): "))
print(f"Сумма цифр: {sum_digits(num)}")

print("-" * 20)

    
numbers_input = input("Введите строку чисел через пробел: ")
nums_list = [int(x) for x in numbers_input.split()]
avg = average(nums_list)
if avg is None:
    print("Нет данных.")
else:
    print(f"Среднее арифметическое: {avg}")
print("-" * 20)

   
text_input = input("Введите произвольный текст: ")
print(f"Нормализованный текст: '{normalize_text(text_input)}'")
print("-" * 20)


nums_list1 = [-5, 0, 2, 5]
print(f"Используется контрольный список: {nums_list1}")
threshold = int(input("Введите порог (целое неотрицательное число): "))
if threshold < 0:
    print("Порог должен быть неотрицательным")
    threshold = 0
result = select_numbers(nums_list1, threshold)
print(f"Результат отбора (числа больше {threshold}): {result}")

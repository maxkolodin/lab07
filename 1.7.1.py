def sum_digits(number):
    number = abs(number)
    if number == 0:
        return 0
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
def normalize_text(text):
    words = text.split()
    return " ".join(words).lower()
def select_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

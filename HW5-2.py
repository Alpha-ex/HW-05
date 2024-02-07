import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
def generator_numbers(text):
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text):
    total_profit = sum(generator_numbers(text))
    return total_profit
total_profit = sum_profit(text)
print("Загальний прибуток:", total_profit)
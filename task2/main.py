import re
from decimal import Decimal
from typing import Callable

def generator_numbers(text: str):
    # regexp for finding float numbers separated by spaces
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield Decimal(match.group())

def sum_profit(text: str, func: Callable):
    # Usage of generator_numbers for sum calculation
    numbers_generator = func(text)
    return sum(numbers_generator, Decimal(0))

def main():
    # sum_profit usage example
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total = sum_profit(text, generator_numbers)
    print("Загальний прибуток:", total)

if __name__ == "__main__":
    main()
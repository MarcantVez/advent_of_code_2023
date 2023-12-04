import re 
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

calib_sum = 0
lines = []

digit_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four' : '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open('input.txt', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    logging.debug(f"Line {i}: {line}")
    # find all single digits numbers and digit spelled with letters in the line
    found_digits = re.findall(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', line)
    # convert all found digits to int
    found_digits = [digit_map[digit] if digit in digit_map else digit for digit in found_digits]
    logging.debug(found_digits)
    calib_sum += int(f"{found_digits[0]}{found_digits[-1]}")

print(calib_sum)
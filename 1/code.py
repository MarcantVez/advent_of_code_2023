import re 
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

calib_sum = 0
lines = []

digit_map = {
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
    # PART 1
    # found_digits = re.findall(r'(?=(\d))', line.rstrip())
    # PART 2
    found_digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line.rstrip())
    # convert all found digits to int
    found_digits = [digit_map[digit] if digit in digit_map else digit for digit in found_digits]
    logging.debug(f"Found digits: {found_digits}")
    # make 2 digit number from first and last digit
    value = int(f"{found_digits[0]}{found_digits[-1]}")
    logging.debug(f"Value: {value}\n\n")
    calib_sum += value

print(calib_sum)
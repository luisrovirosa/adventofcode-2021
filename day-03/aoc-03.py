import numpy as np

lines = open('input.txt').read().split('\n')
bits = [[int(char) for char in line] for line in lines]

def digits(bits: list, criteria: callable):
    digits_array = np.array(bits).T
    sum_digit = [sum(digit_array) for digit_array in digits_array]
    return [criteria(sum) for sum in sum_digit]

def to_decimal(bits: list):
    bits_as_string = [str(num) for num in bits]
    return int(''.join(bits_as_string), 2)

def gamma_digits(bits: list):
    return digits(bits, lambda sum: '1' if sum >= len(bits) / 2 else '0')

def epsilon_digits(bits: list):
    return digits(bits, lambda sum: '0' if sum >= len(bits) / 2 else '1')

gamma_rate = to_decimal(gamma_digits(bits))
print('Gamma_rate', gamma_rate)

epsilon_rate = to_decimal(epsilon_digits(bits))
print('Epsilon_rate', epsilon_rate)

def oxigen_generation_rating(bits: list, function: callable, position: int):
    digit = int(function(bits)[position])
    remaining_bits = list(filter(lambda bit: bit[position] == digit, bits))
    if (len(remaining_bits) > 1):
        return oxigen_generation_rating(remaining_bits, function, position+1)
    return remaining_bits[0]

print('Power consumption', gamma_rate*epsilon_rate)

oxygen = to_decimal(oxigen_generation_rating(bits, gamma_digits, 0))
print('Oxigen', oxygen)
co2 = to_decimal(oxigen_generation_rating(bits, epsilon_digits, 0))
print('CO2', co2)
print('Life support', oxygen * co2)
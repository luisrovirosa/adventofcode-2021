import numpy as np

lines = open('input.txt').read().split('\n')
bits = [[int(char) for char in line] for line in lines]

def digits(bits: list, criteria: callable):
    digits_array = np.array(bits).T
    sum_digit = [sum(digit_array) for digit_array in digits_array]
    return [criteria(sum) for sum in sum_digit]

def to_decimal(bits: list):
    return int(''.join(bits), 2)

def gamma_digits(bits: list):
    return digits(bits, lambda sum: '1' if sum >= len(bits) / 2 else '0')

def epsilon_digits(bits: list):
    return digits(bits, lambda sum: '0' if sum >= len(bits) / 2 else '1')

gamma_rate = to_decimal(gamma_digits(bits))
print('Gamma_rate', gamma_rate)

epsilon_rate = to_decimal(epsilon_digits(bits))
print('Epsilon_rate', epsilon_rate)

print('Power consumption', gamma_rate*epsilon_rate)
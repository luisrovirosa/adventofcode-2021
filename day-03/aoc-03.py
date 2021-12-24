import numpy as np

lines = open('input.txt').read().split('\n')
bits = [[int(char) for char in line] for line in lines]

digits_array = np.array(bits).T

sum_digit = [sum(digit_array) for digit_array in digits_array]
gamma_digits = ['1' if sum > len(lines) / 2 else '0' for sum in sum_digit]
gamma_rate = int(''.join(gamma_digits), 2)
epsilon_digits = ['0' if sum > len(lines) / 2 else '1' for sum in sum_digit]
epsilon_rate = int(''.join(epsilon_digits), 2)

print('Gamma_rate', gamma_rate)
print('Epsilon_rate', epsilon_rate)
print('Power consumption', gamma_rate*epsilon_rate)
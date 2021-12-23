import functools

lines = open('input.txt').read().split('\n')
orders = [line.split(' ') for line in lines]


def movement(command, units, position):
    operations = {
        'forward': lambda: [position[0] + units, position[1] + position[2] * units, position[2]],
        'up': lambda: [position[0], position[1], position[2] - units],
        'down': lambda: [position[0], position[1], position[2] + units],
    }
    return operations[command]()


x, y, aim = functools.reduce(lambda position, order: movement(order[0], int(order[1]), position), orders, [0, 0, 0])

print(x * y)

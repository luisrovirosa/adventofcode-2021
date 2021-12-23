lines = open('input.txt').read().split('\n')
orders = [line.split(' ') for line in lines]


def movement(command, units):
    operations = {
        'forward': lambda: [units, 0],
        'up': lambda: [0, -units],
        'down': lambda: [0, units],
    }
    return operations[command]()


movements = [movement(command, int(units)) for command, units in orders]

x = sum(movement[0] for movement in movements)
y = sum(movement[1] for movement in movements)
print(x*y)
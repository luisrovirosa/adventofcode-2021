measures = open('input.txt').read().split('\n')
res = [int(sub1) < int(sub2) for sub1, sub2 in zip(measures, measures[1:])]
number_of_greater_elements = sum(is_greater for is_greater in res)
print("First answer", number_of_greater_elements)
measures = open('input.txt').read().split('\n')

def number_of_greater_elements(measures):
    res = [int(sub1) < int(sub2) for sub1, sub2 in zip(measures, measures[1:])]
    return sum(is_greater for is_greater in res)

print("First answer", number_of_greater_elements(measures))

sum_three_elements =  [int(sub1) + int(sub2) + int(sub3) for sub1, sub2, sub3 in zip(measures, measures[1:], measures[2:])]
print("Second answer", number_of_greater_elements(sum_three_elements))

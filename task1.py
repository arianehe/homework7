import random

random.seed(2020)

numbers = [random.randint(100, 120) for i in range(20)]

numbers = sorted(numbers, reverse=True)

median = numbers[9]

num_dict = {}

for num in numbers:
    num_dict.setdefault(num, 0)
    num_dict[num] += 1

max_frequency = max(num_dict.values())

mode = []

for key, value in num_dict.items():
    if value == max_frequency:
        mode.append(key)

print("The median is: {}".format(median))
print("The mode(s) is(are): ", end="")
for m in mode:
    print(m, end=" ")
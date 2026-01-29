from random import random

# I generated a list of 20 random values between 0 and 1
values = [random() for i in range(20)]
x = random()  # I generated a random comparison value

# I sorted the list before searching through it
values.sort()

matchingIndices = []

# I used enumerate to check each value and its index
for index, value in enumerate(values):
    if value >= x:
        matchingIndices.append(index)

print("Sorted values:", values)
print("x:", x)

# I printed the first matching index only if one exists
if matchingIndices:
    print("First matching index:", matchingIndices[0])
else:
    print("No value is greater than or equal to x")

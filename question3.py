def computePower(x, y):
    # I created this function to return x raised to the power of y
    return x ** y


pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []  # I used this list to store valid results

for x, y in pairs:
    if y < 0:
        continue

    results.append(computePower(x, y))

# I printed the final list of computed values
print(results)

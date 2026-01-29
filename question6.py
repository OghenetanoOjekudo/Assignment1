def distributionAnalysis(numbers):
    # I added this check to avoid dividing by zero if the list is empty
    if len(numbers) == 0:
        return "Input list cannot be empty."

    totalCount = len(numbers)
    result = {}

    # I used sorted(set(numbers)) to get unique values in order
    for value in sorted(set(numbers)):
        countLessOrEqual = 0

        # I looped through the list to count values less than or equal to the current key
        for n in numbers:
            if n <= value:
                countLessOrEqual += 1

        # I converted the count into a percentage
        percentage = (countLessOrEqual / totalCount) * 100
        result[value] = percentage

    return result


# I used this example to test that the function works correctly
numbers = [3, 1, 2, 3, 4, 2]
print(distributionAnalysis(numbers))

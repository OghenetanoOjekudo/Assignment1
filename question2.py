def buildStringDictionary(stringList):
    result = {}  # I created an empty dictionary to store the results

    # I looped through each string in the input list
    for word in stringList:
        length = len(word)  # I calculated the length of the string

        # I checked whether the length is even or odd
        if length % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        # I stored the length and parity in a nested dictionary
        result[word] = {
            "length": length,
            "parity": parity
        }

    return result


# I used this list to test the function
strings = ["data", "science"]
print(buildStringDictionary(strings))

threshold = 100        # I set the threshold value the product must exceed
product = 1            # I started the product at 1 since we are multiplying
currentNumber = 1      # I started counting from 1

# I used a while loop to keep multiplying until the product exceeds the threshold
while product <= threshold:
    product = product * currentNumber
    currentNumber += 1  # I incremented the number after each multiplication

# I subtracted 1 because currentNumber increases one extra time before the loop stops
print("Final product:", product)
print("Integer that caused it to exceed:", currentNumber - 1)

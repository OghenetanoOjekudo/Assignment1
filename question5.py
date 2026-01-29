import math  # I imported math to use the value of pi

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # I added validation to make sure both radii are positive integers
    if (
        not isinstance(radiusOfCircle1, int)
        or not isinstance(radiusOfCircle2, int)
        or radiusOfCircle1 <= 0
        or radiusOfCircle2 <= 0
    ):
        return "Both radii must be positive integers."

    # I calculated the area of each circle using πr²
    area1 = math.pi * radiusOfCircle1 ** 2
    area2 = math.pi * radiusOfCircle2 ** 2

    # I identified the smaller and larger areas
    smallerArea = min(area1, area2)
    largerArea = max(area1, area2)

    # I calculated the percentage of the larger circle covered by the smaller one
    percentageCovered = (smallerArea / largerArea) * 100

    return percentageCovered


# I used this example to test the function
print(circleAreaCoverage(3, 5))

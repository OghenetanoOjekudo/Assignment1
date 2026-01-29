def convertTime(seconds):
    # I added this check to make sure the input is valid
    if not isinstance(seconds, int) or seconds < 0 or seconds >= 86400:
        return "Invalid input."

    # I used integer division to calculate the hours since midnight
    hours = seconds // 3600

    # I used modulo to get the remaining minutes
    minutes = (seconds % 3600) // 60

    # I used modulo again to get the remaining seconds
    secs = seconds % 60

    # I determined whether the time is AM or PM
    period = "AM" if hours < 12 else "PM"

    # I converted the time to 12-hour format
    hours = hours % 12
    if hours == 0:
        hours = 12

    # I returned the formatted time as a string
    return f"{hours} {minutes} {secs} {period}"


# I used this example to test that the function works correctly
print(convertTime(19067))

for number in range(40):
    print(number * 2)


show_expected_result = False
show_hints = False


def your_code():
    numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

    # Your code goes here.

    length = len(numbers)
    sum = 0

    """
    for index in range (length):
        if numbers[index] % 2 == 0:
            sum = sum + numbers[index]

    """
    while length > 0:
        if numbers[length - 1] % 2 == 0:
            sum = sum + numbers[length - 1]
        length = length - 1

    return sum
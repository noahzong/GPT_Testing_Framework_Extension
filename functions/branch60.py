def branch60(input1, input2):
    # Determine which input is greater
    if input1 > input2:
        result1 = input1 - input2
    elif input2 > input1:
        result1 = input2 - input1
    else:
        result1 = 0

    # Multiply the greater input by 3
    if input1 > input2:
        result2 = input1 * 3
    elif input2 > input1:
        result2 = input2 * 3
    else:
        result2 = 0

    # Divide the greater input by 4
    if input1 > input2:
        result3 = input1 / 4
    elif input2 > input1:
        result3 = input2 / 4
    else:
        result3 = 0

    # Add the two results
    result4 = result2 + result3

    # Check if the result is greater than 10
    if result4 > 10:
        final_result = result4 * 2
    else:
        final_result = result4 / 2

    return final_result
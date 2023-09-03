def branch4(input_1, input_2, input_3):
    if input_1 > 10:
        result_1 = input_1 * 2
    else:
        result_1 = input_1 + 5

    if input_2 < 0:
        result_2 = input_2 * -1
    elif input_2 > 100:
        result_2 = input_2 / 2
    else:
        result_2 = input_2

    if input_3 == "yes":
        result_3 = "Affirmative"
    elif input_3 == "no":
        result_3 = "Negative"
    else:
        result_3 = "Unknown"

    final_result = result_1 + result_2 + result_3
    return final_result
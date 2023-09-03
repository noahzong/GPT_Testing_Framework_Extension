def branch24(input1, input2, input3):
 
    # initialize variables
    output1 = 0
    output2 = 0
    output3 = 0
 
    # if statements
    if input1 == 0:
        output1 = input2 * 2
    elif input1 == 1:
        output1 = input2 * 3
    elif input1 == 2:
        output1 = input2 * 4
    else:
        output1 = input2 * 5
 
    # if/else statements
    if input2 > 0:
        output2 = input2 + input3
    else:
        output2 = input2 - input3
 
    # nested if statements
    if input3 == 0:
        output3 = input1 * 2
        if input2 > 0:
            output3 += 1
        else:
            output3 -= 1
    elif input3 == 1:
        output3 = input1 * 3
        if input2 > 0:
            output3 += 2
        else:
            output3 -= 2
    elif input3 == 2:
        output3 = input1 * 4
        if input2 > 0:
            output3 += 3
        else:
            output3 -= 3
    else:
        output3 = input1 * 5
        if input2 > 0:
            output3 += 4
        else:
            output3 -= 4
 
    return output1, output2, output3
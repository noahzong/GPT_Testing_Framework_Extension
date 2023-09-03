def branch46(var1, var2):
    if var1 == "high":
        if var2 == "low":
            return "Result1"
        elif var2 == "medium":
            return "Result2"
        elif var2 == "high":
            return "Result3"
    elif var1 == "medium":
        if var2 == "low":
            return "Result4"
        elif var2 == "medium":
            return "Result5"
        elif var2 == "high":
            return "Result6"
    elif var1 == "low":
        if var2 == "low":
            return "Result7"
        elif var2 == "medium":
            return "Result8"
        elif var2 == "high":
            return "Result9"
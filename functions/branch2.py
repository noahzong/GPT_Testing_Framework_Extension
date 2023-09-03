def branch2(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    elif 0 < x <= 10:
        return "Small"
    elif 10 < x <= 20:
        return "Medium"
    elif 20 < x <= 30:
        return "Large"
    else:
        return "Very Large"
def branch3(x):
    if x < 0:
        if x < -10:
            return "Very Negative"
        else:
            return "Negative"
    elif x == 0:
        return "Zero"
    elif 0 < x <= 5:
        return "Very Small"
    elif 5 < x <= 10:
        return "Small"
    elif 10 < x <= 15:
        return "Medium Small"
    elif 15 < x <= 20:
        return "Medium"
    elif 20 < x <= 25:
        return "Medium Large"
    elif 25 < x <= 30:
        return "Large"
    elif 30 < x <= 50:
        return "Very Large"
    else:
        return "Extremely Large"
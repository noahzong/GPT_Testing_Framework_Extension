def financial_aid(age, country, income):
    country = country.lower()
    if country == "usa":
        if age >= 18:
            if income < 50000:
                return "You are eligible for financial aid."
            elif 50000 <= income < 100000:
                return "You are eligible for partial financial aid."
            else:
                return "You are not eligible for financial aid."
        else:
            return "You are not eligible for financial aid because you are under 18."
    elif country == "canada":
        if age >= 18:
            if income < 30000:
                return "You are eligible for financial aid."
            elif 30000 <= income < 60000:
                return "You are eligible for partial financial aid."
            else:
                return "You are not eligible for financial aid."
        else:
            return "You are not eligible for financial aid because you are under 18."
    else:
        return "Sorry, we do not have information for your country."
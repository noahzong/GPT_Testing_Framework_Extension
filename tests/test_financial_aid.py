from functions.financial_aid import financial_aid
import pytest

@pytest.mark.parametrize("age, country, income, expected", [
    (17, "USA", 40000, "You are not eligible for financial aid because you are under 18."),
    (18, "USA", 40000, "You are eligible for financial aid."),
    (18, "USA", 50000, "You are eligible for partial financial aid."),
    (18, "USA", 60000, "You are not eligible for financial aid."),
    (17, "Canada", 20000, "You are not eligible for financial aid because you are under 18."),
    (18, "Canada", 20000, "You are eligible for financial aid."),
    (18, "Canada", 30000, "You are eligible for partial financial aid."),
    (18, "Canada", 40000, "You are not eligible for financial aid."),
    (18, "Mexico", 40000, "Sorry, we do not have information for your country.")
])
def test_financial_aid(age, country, income, expected):
    assert financial_aid(age, country, income) == expected
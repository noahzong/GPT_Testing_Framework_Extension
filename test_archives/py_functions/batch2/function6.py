def function6(name, age, is_member, num_items):
    """
    This function calculates the total cost of an item based on various factors. 

    Parameters:
    name (str): name of user
    age (int): age of user
    is_member (bool): if user is a member
    num_items (int): number of items purchased

    Returns:
    total_cost (float): total cost of items
    """

    base_price = 10.0
    discount_rate = 0.1
    tax_rate = 0.05

    if is_member:
        discount = base_price * discount_rate * num_items
    else:
        discount = 0.0
    
    subtotal = base_price * num_items - discount
    tax = subtotal * tax_rate
    total_cost = subtotal + tax
    
    print(f"{name}, your total cost for {num_items} items is ${total_cost:.2f}.")
    return total_cost
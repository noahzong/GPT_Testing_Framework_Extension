def branch11(base_price, is_discounted, has_shipping, shipping_location):
    # Applying discount if applicable
    if is_discounted:
        discount = 0.2  # 20% discount
        base_price -= base_price * discount
    
    # Adding shipping cost based on location
    if has_shipping:
        if shipping_location == "domestic":
            shipping_cost = 5
        elif shipping_location == "international":
            shipping_cost = 15
        else:
            shipping_cost = 0
    else:
        shipping_cost = 0
    
    # Calculating taxes
    tax_rate = 0.1  # 10% tax
    tax_amount = base_price * tax_rate
    
    # Total cost calculation
    total_cost = base_price + shipping_cost + tax_amount
    
    return total_cost
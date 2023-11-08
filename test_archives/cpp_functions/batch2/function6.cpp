# C++ Code
#include <iostream>
#include <string>

double function6(std::string name, int age, bool is_member, int num_items) {
    double base_price = 10.0;
    double discount_rate = 0.1;
    double tax_rate = 0.05;
    double discount;
    
    if (is_member) {
        discount = base_price * discount_rate * num_items;
    } else {
        discount = 0.0;
    }
    
    double subtotal = base_price * num_items - discount;
    double tax = subtotal * tax_rate;
    double total_cost = subtotal + tax;
    
    std::cout << name << ", your total cost for " << num_items << " items is $" << total_cost << std::endl;
    return total_cost;
}
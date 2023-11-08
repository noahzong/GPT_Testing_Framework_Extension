#include <iostream>
using namespace std;

class function3
{
public:
    // Initializing the Class
    function3(string name, int age, string gender, string address, int phone_number)
    {
        this->name = name;
        this->age = age;
        this->gender = gender;
        this->address = address;
        this->phone_number = phone_number;
        this->total_value = 0;
    }
    
    // Method to Calculate the Final Value 
    int calculate_value()
    {
        // Calculating the Final Value
        this->total_value = this->age + this->phone_number;
        return this->total_value;
    }
    
    // Class Variables
    string name;
    int age;
    string gender;
    string address;
    int phone_number;
    int total_value;
};
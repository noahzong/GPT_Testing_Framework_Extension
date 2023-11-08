# C++ Code

#include <iostream>
#include <string>

int function3(std::string string1, int int1, float float1)
{
    int int2 = int1 * float1;
    if (string1 == "yes")
    {
        int2 += 10;
    }
    else if (string1 == "no")
    {
        int2 -= 5;
    }
    return int2;
}
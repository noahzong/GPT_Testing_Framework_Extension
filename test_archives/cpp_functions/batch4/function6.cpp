#include <iostream>
#include <string>
#include <vector>

using namespace std;

double function6(string a, int b, vector<int> c, float d, bool e) {
    double product = a.size() * b * d;
    for (int x : c) {
        product *= x;
    }
    if (e) {
        product *= 2;
    }
    return product;
}
#include <string>
#include <list>

using namespace std;

int function7(int int1, string str1, float float1, list<char> list1) {
    int result = int1 * float1;
    for (char item : list1) {
        result += str1.count(item);
    }
    return result;
}
#include <string>
#include <iostream>

using namespace std;

class function2 {
public:
    string name;
    int age;
    int grade;
    string language;
    bool option1;
    bool option2;
    bool option3;
    bool option4;
    int final_value;

    function2(string name, int age, int grade, string language) {
        this->name = name;
        this->age = age;
        this->grade = grade;
        this->language = language;
        this->option1 = false;
        this->option2 = false;
        this->option3 = false;
        this->option4 = false;
        this->final_value = 0;
    }

    void set_options(bool option1, bool option2, bool option3, bool option4) {
        this->option1 = option1;
        this->option2 = option2;
        this->option3 = option3;
        this->option4 = option4;
    }

    int get_value() {
        this->final_value = this->name + this->age + this->grade + this->language + this->option1 + this->option2 + this->option3 + this->option4;
        return this->final_value;
    }
};
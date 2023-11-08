class function2:
    def __init__(self, name, age, grade, language):
        self.name = name
        self.age = age
        self.grade = grade
        self.language = language
        self.option1 = False
        self.option2 = False
        self.option3 = False
        self.option4 = False
        self.final_value = 0
        
    def set_options(self, option1, option2, option3, option4):
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        
    def get_value(self):
        self.final_value = self.name + self.age + self.grade + self.language + self.option1 + self.option2 + self.option3 + self.option4
        return self.final_value
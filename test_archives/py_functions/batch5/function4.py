class function4:
    
    def __init__(self, name, age, gender, income):
        self.name = name
        self.age = age
        self.gender = gender
        self.income = income
        self.list1 = []
        self.list2 = []
        self.dict1 = {}
        self.dict2 = {}
        self.str1 = ""
        self.str2 = ""
        self.int1 = 0
        self.int2 = 0
        self.float1 = 0.0
        self.float2 = 0.0
        self.char1 = ''
        self.char2 = ''
        
    def calculate_final_value(self):
        final_value = self.int1 + self.int2 + float(self.float1) + float(self.float2) + len(self.list1) + len(self.list2) + len(self.dict1) + len(self.dict2) + len(self.str1) + len(self.str2) + ord(self.char1) + ord(self.char2)
        return final_value
class function1:
    
    def __init__(self, string1, int1, float1, boolean1, list1):
        self.string1 = string1
        self.int1 = int1
        self.float1 = float1
        self.boolean1 = boolean1
        self.list1 = list1
        
    def compute(self):
        final_value = self.string1 + str(self.int1) + str(self.float1) + str(self.boolean1) + str(self.list1)
        return final_value
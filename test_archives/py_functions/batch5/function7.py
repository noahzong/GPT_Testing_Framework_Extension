class function7():
    def __init__(self, user_input1, user_input2, user_input3):
        self.user_input1 = user_input1
        self.user_input2 = user_input2
        self.user_input3 = user_input3
        self.string1 = ""
        self.list1 = []
        self.int1 = 0
        self.float1 = 0.0
        self.dict1 = {}
        self.boolean1 = False

    def method1(self):
        # do something with user inputs
        self.string1 = self.user_input1 + self.user_input2
        self.list1 = [self.user_input1, self.user_input2, self.user_input3]
        self.int1 = len(self.list1)
        self.float1 = self.int1 / 2
        self.dict1 = {self.user_input1: self.user_input2, self.user_input2: self.user_input3}
        self.boolean1 = True

    def method2(self):
        # do something else
        final_value = self.string1 + str(self.int1) + str(self.float1) + str(self.dict1)
        return final_value
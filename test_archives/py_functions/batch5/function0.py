class function0:
    def __init__(self, int_input, float_input, string_input, list_input):
        self.integer = int_input
        self.float = float_input
        self.string = string_input
        self.list = list_input
        self.dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.tuple = (1, 2, 3)
        self.set = {1, 2, 3}
 
    def multiply_result(self):
        result = self.integer * self.float
        for i in self.list:
            result *= i
        return result
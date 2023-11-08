class function6():
   
    def __init__(self, num1, num2, str1, str2, lst1, lst2):
        self.num1 = num1
        self.num2 = num2
        self.str1 = str1
        self.str2 = str2
        self.lst1 = lst1
        self.lst2 = lst2

    def get_sum(self):
        return self.num1 + self.num2

    def get_concat(self):
        return self.str1 + self.str2

    def get_lst_avg(self):
        lst_sum = 0
        for val in self.lst1 + self.lst2:
            lst_sum += val
        return lst_sum / (len(self.lst1) + len(self.lst2))
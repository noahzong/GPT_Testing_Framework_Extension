class function8():
    """
    Sample Python class with a lot of variables and data types.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.str_var = "variable"
        self.int_var = 0
        self.float_var = 0.0
        self.bool_var = False
        self.list_var = []
        self.tuple_var = ()
        self.dict_var = {}

    def combine_vars(self):
        """
        Returns the combination of all variables as a single value.
        """
        return self.str_var + str(self.int_var) + str(self.float_var) + str(self.bool_var) + str(self.list_var) + str(self.tuple_var) + str(self.dict_var) + str(self.x) + str(self.y) + str(self.z)
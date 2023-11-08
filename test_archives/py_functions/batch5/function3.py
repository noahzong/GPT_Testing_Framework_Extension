class function3:
    # Initializing the Class
    def __init__(self, name, age, gender, address, phone_number):
        self.name = name 
        self.age = age 
        self.gender = gender 
        self.address = address 
        self.phone_number = phone_number 
        self.total_value = 0 
        
    # Method to Calculate the Final Value 
    def calculate_value(self):
        # Calculating the Final Value
        self.total_value = self.age + self.phone_number 
        return self.total_value
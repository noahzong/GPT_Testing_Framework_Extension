class function5:
  def __init__(self, input_string, input_int, input_float, input_bool):
    self.input_string = input_string
    self.input_int = input_int
    self.input_float = input_float
    self.input_bool = input_bool
    self.list_1 = []
    self.list_2 = []
    self.dict_1 = {}
    self.dict_2 = {}

  def process_data(self):
    result = 0
    for i in range(self.input_int):
      result += self.input_float * (i + 1)

    if self.input_bool:
      result += len(self.input_string)

    return result
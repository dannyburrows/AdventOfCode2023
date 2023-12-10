class LineSum:
  def get_sum(self, text):
    lines = text.split("\n")
    sum = 0
    for line in lines:
      sum += self.get_sum_for_line(line)
    return sum

  def get_left(self, input):
    for s in input:
      if s.isdigit():
        return s
    return 0

  def get_right(self, input):
    for s in input[::-1]:
      if s.isdigit():
        return s
    return 0

  def get_sum_for_line(self, input):
    result = int(self.get_left(input) + self.get_right(input))
    return result

class GetData:
  def get_data(self):
    with open("./data.txt", "r") as file:
      return file.read()

def main():
  data = GetData()
  input = data.get_data()
  sum_string = LineSum()
  print(sum_string.get_sum(input))

if __name__ == '__main__':
  main()
import re

class LineSum:
  valid_digits = [
    r'one',
    r'two',
    r'three',
    r'four',
    r'five',
    r'six',
    r'seven',
    r'eight',
    r'nine',
    r'1',
    r'2',
    r'3',
    r'4',
    r'5',
    r'6',
    r'7',
    r'8',
    r'9'
  ]
  pattern = None

  word_to_digit = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9"
  }

  def __init__(self) -> None:
    self.pattern = r'(?:' + '|'.join(re.escape(digit) for digit in self.valid_digits) + r')'

  def get_sum(self, text):
    lines = text.split("\n")
    sum = 0
    for line in lines:
      sum += self.get_sum_for_line(line)
    return sum

  def get_left(self, input):
    match = re.search(self.pattern, input, flags=re.IGNORECASE)
    if match is not None and match.group().isdigit():
      return match.group()
    elif match is not None:
      return self.word_to_digit[match.group()]
    return 0

  def get_right(self, input):
    matches = [match.group() for match in re.finditer(self.pattern, input, flags=re.IGNORECASE)]
    last_match = matches[-1]
    if last_match.isdigit():
      return last_match
    elif last_match is not None:
      return self.word_to_digit[last_match]
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
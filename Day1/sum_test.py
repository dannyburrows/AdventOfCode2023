import unittest
from sum_string import LineSum

class TestSum(unittest.TestCase):
  input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

  def test_sum(self):
    sum_string = LineSum()
    self.assertEqual(sum_string.get_sum(self.input), 281, "Should be 281")

  def test_line_sum(self):
    sum_string = LineSum()
    self.assertEqual(sum_string.get_sum_for_line("four1four"), 44, "Should be 44")

  def test_get_left(self):
    sum_string = LineSum()
    self.assertEqual(sum_string.get_left("seven-8one"), "7", "Should be 7")

  def test_get_right(self):
    sum_string = LineSum()
    self.assertEqual(sum_string.get_right("seven-8one"), "1", "Should be 1")

if __name__ == '__main__':
    unittest.main() 
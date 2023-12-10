import unittest
from sum_string import LineSum

class TestSum(unittest.TestCase):
  input = """
      1abc2
      pqr3stu8vwx
      a1b2c3d4e5f
      treb7uchet
    """

  def test_sum(self):
    sum_string = LineSum()
    self.assertEqual(sum_string.get_sum(self.input), 142, "Should be 142")

  def test_line_sum(self):
    sum_string = LineSum()
    self.assertEqual(sum_string.get_sum_for_line("input7-8input"), 78, "Should be 78")

if __name__ == '__main__':
    unittest.main()
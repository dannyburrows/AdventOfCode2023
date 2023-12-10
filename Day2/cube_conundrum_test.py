import unittest
from cube_conundrum import Cube, GameSubset, Game, GameSum

class TestGameSum(unittest.TestCase):
  test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

  def test(self):
    self.assertEqual(0, 0, "Should be 0")

class TestGame(unittest.TestCase):
  def test_parse_text(self):
    game = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    self.assertTrue(game.game_number == 1, "Should be 1")
    self.assertTrue(len(game.subsets) == 3, "Should be 3")
  
  def test_is_valid(self):
    game = Game("Game 1: 15 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    self.assertFalse(game.is_valid(), "Should be False")
  
  def test_find_mins(self):
    game = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 7 green")
    game.find_mins()
    game.min_colors['blue'] = 6
    game.min_colors['red'] = 4
    game.min_colors['green'] = 7

class TestGameSubset(unittest.TestCase):
  def test_parse_subset(self):
    subset = GameSubset("3 blue, 4 red;")
    self.assertEqual(subset.green.number, 0, "Should be 0")
    self.assertEqual(subset.blue.number, 3, "Should be 3")
    self.assertEqual(subset.red.number, 4, "Should be 4")

  def test_is_valid(self):
    subset1 = GameSubset("15 blue")
    self.assertFalse(subset1.is_valid(), "Should be False")
    subset2 = GameSubset("15 red")
    self.assertFalse(subset2.is_valid(), "Should be False")
    subset3 = GameSubset("15 green")
    self.assertFalse(subset3.is_valid(), "Should be False")

class TestCube(unittest.TestCase):
  def test_is_valid(self):
    valid_cube = Cube('red', 12)
    invalid_cube = Cube('red', 13)
    self.assertTrue(valid_cube.is_valid(), "Should be True")
    self.assertFalse(invalid_cube.is_valid(), "Should be False")
  
if __name__ == '__main__':
    unittest.main()
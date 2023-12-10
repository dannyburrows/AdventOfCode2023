import re

class Cube:
  possible_max = {
    'red': 12,
    'green': 13,
    'blue': 14
  }

  def __init__(self, color, number):
    self.color = color
    self.number = number
  
  def is_valid(self):
    return self.number <= self.possible_max[self.color]    

class GameSubset:
  def __init__(self, game_subset_text):
    self.red = Cube('red', 0)
    self.green = Cube('green', 0)
    self.blue = Cube('blue', 0)
    self.game_subset_text = game_subset_text
    self.parse_subset()
  
  def parse_subset(self):
    regex_pattern = re.compile(r'(\d+)\s+([a-zA-Z]+)')
    matches = regex_pattern.findall(self.game_subset_text)
    for match in matches:
      number = int(match[0])
      color = match[1]
      if color == 'red':
        self.red.number = number
      elif color == 'green':
        self.green.number = number
      elif color == 'blue':
        self.blue.number = number
      else:
        raise Exception("Invalid color")
  
  def is_valid(self):
    return self.red.is_valid() and self.green.is_valid() and self.blue.is_valid()

# Game should have 3 cubes, one for each color
class Game:
  def __init__(self, game_text):
    self.game_text = game_text
    self.game_number = None # stores game number to be used during summation
    self.subsets = [] # stores GameSubset objects
    self.min_colors = {'red': 0, 'green': 0, 'blue': 0} # stores min number of cubes for each color
    self.parse_text()
  
  def parse_text(self):
    # find game number
    regex_pattern = re.compile(r'Game\s+(\d+)')
    match = regex_pattern.search(self.game_text)
    if match is not None:
      self.game_number = int(match.group(1))
    else:
      raise Exception("Invalid game number")
    # find number of games
    subsets = self.game_text.replace(match.group() + ":", "").split(';')
    for subset in subsets:
      self.subsets.append(GameSubset(subset))
  
  def find_mins(self):
    for subset in self.subsets:
      if subset.red.number > self.min_colors['red']:
        self.min_colors['red'] = subset.red.number
      if subset.green.number > self.min_colors['green']:
        self.min_colors['green'] = subset.green.number
      if subset.blue.number > self.min_colors['blue']:
        self.min_colors['blue'] = subset.blue.number
  
  def get_power_sum(self):
    self.find_mins()
    return self.min_colors['red'] * self.min_colors['green'] * self.min_colors['blue']
  
  def is_valid(self):
    for subset in self.subsets:
      if not subset.is_valid():
        return False
    return True

class GameSum:
  def __init__(self) -> None:
    self.games = []
    self.games_text = self.get_data()
    self.build_games()

  def build_games(self):
    games = self.games_text.split("\n")
    for game in games:
      self.games.append(Game(game))

  def get_data(self):
    with open("./data.txt", "r") as file:
      return file.read()
    
  def get_power_sum(self):
    sum = 0
    for game in self.games:
      sum += game.get_power_sum()
    return sum

  def get_sum(self):
    sum = 0
    for game in self.games:
      if game.is_valid():
        sum += game.game_number
    return sum # 2683
    
def main():
  game_sum = GameSum()
  print("Sum", game_sum.get_sum())
  print("Power Sum", game_sum.get_power_sum())

if __name__ == '__main__':
  main()
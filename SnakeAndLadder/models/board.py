
class SnakeAndLadderBoard(object):
  def __init__(self, size):
    self.size = size
    self.snakes = None
    self.ladders = None
    self.player_cur_pos = {}

  def getPlayerCurPos(self, player_name):
    return self.player_cur_pos[player_name]
  
  def setPlayerCurPos(self, player_name, cur_pos):
    self.player_cur_pos[player_name] = cur_pos
  
  def getSnakes(self):
    return self.snakes

  def setSnakes(self, snakes):
    self.snakes = snakes

  def setLadders(self, ladders):
    self.ladders = ladders

  def getLadders(self):
    return self.ladders
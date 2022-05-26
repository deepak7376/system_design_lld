from models.board import SnakeAndLadderBoard
from services.dice_service import DiceService


class SnakeAndLadderService(object):
  def __init__(self, size):
    self.size = size
    self.board = None
    self.players = []

  ## setter logic
  def setBoard(self):
    self.board = SnakeAndLadderBoard(self.size)

  def setPlayers(self, players):
    for player_name in players:
      self.board.setPlayerCurPos(player_name, 0)
    self.players = players

  def setSnakes(self, snakes):
    self.board.setSnakes(snakes) 

  def setLadders(self, ladders):
    self.board.setLadders(ladders)

  ## game logic

  def getNewPostion(self, new_pos):
    prev_pos = None

    while prev_pos !=new_pos:
      prev_pos = new_pos
      # search for snakes or ladder
      for snake in self.board.getSnakes():
        if new_pos == snake.getStart():
          new_pos = snake.getEnd()

      for ladder in self.board.getLadders():
        if new_pos == ladder.getStart():
          new_pos = ladder.getEnd()

      return new_pos


  def movePlayer(self, player_name, pos):
    cur_pos = self.board.getPlayerCurPos(player_name)
    new_pos = cur_pos + pos

    if new_pos>self.size:
      new_pos = cur_pos

    else:
      new_pos = self.getNewPostion(new_pos)
    
    print(f"{player_name.getName()} rolled a {pos} and moved from {cur_pos} to {new_pos}")

    self.board.setPlayerCurPos(player_name, new_pos)
    

  def isGameEnd(self):
    return False

  def isPlayerWon(self, player_name):
    if self.board.getPlayerCurPos(player_name)==self.size:
      return True
    return False

  def getTotalValueAfterDiceRoll(self):
    return DiceService().roll()

  def start(self):

    while self.isGameEnd()==False:
      player_name = self.players.pop(0)
      total_dice_value_after_roll = self.getTotalValueAfterDiceRoll()
      self.movePlayer(player_name, total_dice_value_after_roll)
      if self.isPlayerWon(player_name):
        print(f"{player_name.getName()} wins the game")
        break

      self.players.append(player_name)
      

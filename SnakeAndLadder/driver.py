import sys
sys.path.insert(0,'/Users/activainc/Desktop/system_design_lld/')

from services.snake_and_board_service import SnakeAndLadderService
from models.snake import Snake
from models.player import Player
from models.ladder import Ladder


snakes = []
snakes.append(Snake(62, 5))
snakes.append(Snake(33 ,6))
snakes.append(Snake(49, 9))
snakes.append(Snake(88, 16))
snakes.append(Snake(41, 20))
snakes.append(Snake(56, 53))
snakes.append(Snake(98, 64))
snakes.append(Snake(93, 73))
snakes.append(Snake(95, 75))

ladders = []
ladders.append(Ladder(2, 37))
ladders.append(Ladder(27, 46))
ladders.append(Ladder(10, 32))
ladders.append(Ladder(51, 68))
ladders.append(Ladder(61, 79))
ladders.append(Ladder(65, 84))
ladders.append(Ladder(71, 91))
ladders.append(Ladder(81, 100))

players = []
players.append(Player("Gavrav"))
players.append(Player("Sagar"))

obj = SnakeAndLadderService(100)
obj.setBoard()
obj.setSnakes(snakes)
obj.setLadders(ladders)
obj.setPlayers(players)

obj.start()
















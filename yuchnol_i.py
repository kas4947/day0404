import random

class Dice:

    def __init__(self):
        pass

    def roll(self):
        return random.randrange(1, 6)

class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.unit = 3

class Tile:

    def __init__(self, number):
        self.num = number


class GameBoard:

    def __init__(self):
        self.tiles = [ Tile(x) for x in range(1, 22)]


    def movePlayer(self,p , amount):

        visit_tiles = []

        print('debug: ' ,p , amount)
        value = p.position + amount

        current = self.tiles[value]
        visit_tiles.append(current)



class GameUI:

    def __init__(self):
        self.player_list = []
        self.dice = Dice()
        self.board = GameBoard()

    def createPlayer(self):

        player_count = int(input('플레이어를 몇명 생성 하시겠습니까?'))

        for x in range(player_count):
            player_name = str(input("플레이어 이름: "))
            players = Player(player_name)
            print(players)
            self.player_list.append(players)

    def playGame(self):

        count = 0


        while True:

            current_player = self.player_list[count % len(self.player_list)]
            print(current_player.name, " 차례입니다.")
            input("윷을 던집니다.")
            value = self.dice.roll()

            if value == 1:
                print('도')

            elif value == 2:
                print('개')

            elif value == 3:
                print('걸')

            elif value == 4:
                print('윷')

            elif value == 5:
                print('모')

            count += 1

            visite_result = self.board.movePlayer(current_player, value)

            print(visite_result, '째 자리에 도착하였습니다.')


game = GameUI()
game.createPlayer()
game.playGame()
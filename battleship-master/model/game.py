from.list_de import ListDE
from.user import User
from .board import Board

class Game:
    def __init__(self,player1:User,player2:User,ship_list:ListDE,id:int):
        self.id=id
        self.player1=player1
        self.player2=player2
        self.num_ships=ship_list.count
        self.turn=0
        self.hits_player1=0
        self.hits_player2=0
        self.board_player1=None
        self.board_player2=None
        self.__create__boards(ship_list)

    def __create__boards(self,ship_list:ListDE):
        size=0
        if self.num_ships < 10:
            size=10
        elif self.num_ships < 20:
            size=20
        else:
            size =30
        self.board_player1=Board(1,10,10,self.player1,ship_list)
        self.board_player2 = Board(2, 10, 10, self.player2, ship_list.clone_list())


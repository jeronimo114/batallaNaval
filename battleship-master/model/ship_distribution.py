from.ship import Ship

class ShipDistribution:
    def __init__(self,ship:Ship):
        self.places=[]
        self.ship=ship
        self.orientation=0
        self.state="FREE"



    def validate_coordinate(self,coordinate):
        for coord in self.places:
            if coord.x==coordinate.x and coord.y==coordinate.y:
                return True
        return False
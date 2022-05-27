class Ship:
    def __init__(self,data, id:int):
        if 'name' in data and 'num_places' in data:
            self.name= data['name']
            self.num_places = data['num_places']
            self.id = id
        else:
            raise Exception("Atributos no válidos para barco")

    def ship(self):
        name = "littleship"
        num_places=1
        return num_places, name

    def shiptwoplaces(self):
        name="twoplacesship"
        num_places=2
        return num_places,name

    def shipthreeplaces(self):
        name="shipthreeplaces"
        num_places=3
        return num_places,name

    def shipfourplaces(self):
        name = "shipfourplaces"
        num_places = 4
        return num_places, name

    def shipfiveplaces(self):
        name = "shipfiveplaces"
        num_places = 5
        return num_places, name



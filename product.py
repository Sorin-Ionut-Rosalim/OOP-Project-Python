from json import JSONEncoder


# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__



    # define the Product class, which is the base class for all the  products in the store


class Product:
    def __init__(self, name):
        self.name = name

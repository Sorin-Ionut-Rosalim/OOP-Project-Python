from json import JSONEncoder, JSONDecoder, JSONDecodeError, dump, loads
from product import Product


class Encoder(JSONEncoder):
    """From Python object we need to obtain a JSON representation"""

    def default(self, o):
        return o.__dict__


class Decoder(JSONDecoder):
    """Transform serialized string into Python object"""

    def decode(self, obj, **kwargs):
        data = loads(obj)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        rec = Receiver(*vals)
        return rec


class Receiver(Product):
    recs = []

    @classmethod
    def remove_receiver(cls, rec) -> None:
        """
        Remove a receiver from the product collection.
        param rec: receiver object to be removed
        type rec: Receiver

        return: None
        """
        cls.load_receivers()
        if rec in cls.recs:
            cls.recs.remove(rec)
            with open("receivers.txt", "w") as f:
                for rec in cls.recs:
                    e = Encoder()
                    encoded_rec = e.encode(rec)
                    dump(encoded_rec, f)
                    f.write("\n")

    @classmethod
    def add_receiver(cls, rec) -> None:
        if type(rec) != Receiver:
            return None

        if rec not in cls.recs:
            with open("receivers.txt", "a") as f:
                e = Encoder()
                encoded_rec = e.encode(rec)
                dump(encoded_rec, f)
                f.write("\n")

    @classmethod
    def load_receivers(cls) -> list:
        """
       Load the collection from serialized json to memory.

       return: a list with all the receivers stored in the memory
       rtype: list
       """
        decoder = Decoder()

        try:
            cls.recs = []
            with open("receivers.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_rec = decoder.decode(data, )
                    cls.recs.append(decode_rec)
        except (JSONDecodeError, FileNotFoundError):
            cls.recs = []
        return cls.recs

    def __init__(self, name: str, color: str, channels: int, size: int):
        Product.__init__(self, name)
        self.color = color
        self.channels = channels
        self.size = size

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.name} {self.color} {self.channels} {self.size}'

    def __eq__(self, obj) -> bool:
        if type(self) == type(obj):
            return self.name == obj.name and self.color == obj.color and self.channels == obj.channels and self.size == obj.size
        return False

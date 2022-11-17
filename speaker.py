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
        spk = Speaker(*vals)
        return spk


class Speaker(Product):
    spks = []

    @classmethod
    def remove_speaker(cls, spk) -> None:
        """
        Remove a speaker from the product collection.
        param spk: speaker object to be removed
        type spk: Speaker

        return: None
        """
        cls.load_speakers()
        if spk in cls.spks:
            cls.spks.remove(spk)
            with open("speakers.txt", "w") as f:
                for spk in cls.spks:
                    e = Encoder()
                    encoded_spk = e.encode(spk)
                    dump(encoded_spk, f)
                    f.write("\n")

    @classmethod
    def add_speaker(cls, spk) -> None:
        if type(spk) != Speaker:
            return None

        if spk not in cls.spks:
            with open("speakers.txt", "a") as f:
                e = Encoder()
                encoded_spk = e.encode(spk)
                dump(encoded_spk, f)
                f.write("\n")

    @classmethod
    def load_speakers(cls) -> list:
        """
       Load the collection from serialized json to memory.

       return: a list with all the speakers stored in the memory
       rtype: list
        """
        decoder = Decoder()

        try:
            cls.spks = []
            with open("speakers.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_spk = decoder.decode(data, )
                    cls.spks.append(decode_spk)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.spks = []
        return cls.spks

    def __init__(self, name: str, power: str, wheight: int, size: int):
        Product.__init__(self, name)
        self.power = power
        self.wheight = wheight
        self.size = size

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.name} {self.power} {self.wheight} {self.size}'

    def __eq__(self, obj) -> bool:
        if type(self) == type(obj):
            return self.name == obj.name and self.power == obj.power and self.wheight == obj.wheight and self.size == obj.size
        return False

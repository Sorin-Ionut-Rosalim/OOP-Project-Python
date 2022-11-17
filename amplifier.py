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
        amp = Amplifier(*vals)
        return amp


class Amplifier(Product):
    amps = []

    @classmethod
    def remove_amplifier(cls, amp) -> None:
        """
        Remove an amplifier from the product collection.
        param amp: amplifier object to be removed
        type amp: Amplifier

        return: None
        """
        cls.load_amplifiers()
        if amp in cls.amps:
            cls.amps.remove(amp)
            with open("amplifiers.txt", "w") as f:
                for amp in cls.amps:
                    e = Encoder()
                    encoded_amp = e.encode(amp)
                    dump(encoded_amp, f)
                    f.write("\n")

    @classmethod
    def add_amplifier(cls, amp):
        if type(amp) != Amplifier:
            return None

        if amp not in cls.amps:
            with open("amplifiers.txt", "a") as f:
                e = Encoder()
                encoded_amp = e.encode(amp)
                dump(encoded_amp, f)
                f.write("\n")

    @classmethod
    def load_amplifiers(cls) -> list:
        """
        Load the collection from serialized json to memory.

        return: a list with all the amplifiers stored in the memory
        rtype: list
        """
        decoder = Decoder()

        try:
            cls.amps = []
            with open("amplifiers.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_amp = decoder.decode(data, )
                    cls.amps.append(decode_amp)
        except (JSONDecodeError, FileNotFoundError):
            cls.amps = []
        return cls.amps

    def __init__(self, name: str, power: str, channels: str, size: str):
        Product.__init__(self, name)
        self.power = power
        self.channels = channels
        self.size = size

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.name} {self.power} {self.channels}'

    def __eq__(self, obj) -> bool:
        if type(self) == type(obj):
            return self.name == obj.name and self.power == obj.power and self.channels == obj.channels
        return False

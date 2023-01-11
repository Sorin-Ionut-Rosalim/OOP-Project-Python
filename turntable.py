from json import JSONEncoder, JSONDecoder, JSONDecodeError, dump, loads
from product import Product


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Decoder(JSONDecoder):
    def decode(self, obj, **kwargs):
        data = loads(obj)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        turntable = Turntable(*vals)
        return turntable


class Turntable(Product):
    turntables = []

    @classmethod
    def remove_turntable(cls, turntable):
        cls.load_turntables()
        if turntable in cls.turntables:
            cls.turntables.remove(turntable)
            with open("turntables.txt", "w") as f:
                for turntable in cls.turntables:
                    e = Encoder()
                    encoded_tur = e.encode(turntable)
                    dump(encoded_tur, f)
                    f.write("\n")

    @classmethod
    def add_turntable(cls, turntable) -> None:
        if type(turntable) != Turntable:
            return None

        if turntable not in cls.turntables:
            with open("turntables.txt", "a") as f:
                e = Encoder()
                encoded_tur = e.encode(turntable)
                dump(encoded_tur, f)
                f.write("\n")

    @classmethod
    def load_turntables(cls) -> list:
        decoder = Decoder()

        try:
            cls.turntables = []
            with open("turntables.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_tur = decoder.decode(data, )
                    cls.turntables.append(decode_tur)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.turntables = []
        return cls.turntables

    def __init__(self, name: str, speed: int, conn: int, size: int):
        Product.__init__(self, name)
        self.speed = speed
        if conn == 0:
            self.conn = "Wired"
        else:
            self.conn = "Bluetooth"
        self.size = size

    def __str__(self):
        return f'{type(self).__name__}: {self.name} {self.speed} {self.conn} {self.size}'

    def __eq__(self, obj):
        if type(self) == type(obj):
            return self.name == obj.name and self.speed == obj.speed and self.conn == obj.conn and self.size == obj.size
        return False

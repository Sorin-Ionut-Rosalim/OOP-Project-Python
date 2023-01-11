import datetime
from json import JSONEncoder, JSONDecoder, JSONDecodeError, dump, loads

from amplifier import Amplifier
from receiver import Receiver
from speaker import Speaker
from turntable import Turntable


class Encoder(JSONEncoder):
    @staticmethod
    def custom(object:  Amplifier | Receiver | Speaker | Turntable, customer: str, address: str, _id: str):
        object.__dict__['category'] = type(object).__name__
        object.__dict__['customer'] = customer
        object.__dict__['address'] = address
        object.__dict__['id'] = _id
        return object.__dict__


class Decoder(JSONDecoder):
    def decode(self, obj: dict) -> Amplifier | Receiver | Speaker | Turntable:
        data = obj
        vals = []
        for key in data.keys():
            if key != 'category' and key != 'customer' and key != 'address' and key != 'id':
                vals.append(data[key])
        amp = eval(f'{data["category"]}{*vals,}')
        return amp

    @staticmethod
    def custom_decode(obj: dict) -> list:
        data = obj
        vals = []
        for key in data.keys():
            vals.append(data[key])
        return vals


class Order:

    def __init__(self, customer: str, address: str, products: list = None, _id: str = None) -> None:
        if products is None:
            products = []
        self.products = products
        self.customer = customer
        self.address = address
        if _id is None:
            self.order_date = str(
                datetime.datetime.now().strftime("#%d%m%Y%H%M%S"))
        elif _id == '':
            self.order_date = ''
        else:
            self.order_date = _id

    @classmethod
    def load_order(cls, file: str):
        """
        Method used to create a method using only the file representation saved on the disk
        :param file: string that represent the name of the file
        :return: an Order object
        """
        decoder = Decoder()
        products = []
        try:
            with open(f'orders/{file}', 'r') as f:
                for line in f:
                    data = loads(line)
                    decoded_order = decoder.custom_decode(data)
                    products.append(decoder.decode(data, ))

                return Order(decoded_order[5], decoded_order[6], products, decoded_order[-1])
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.categories = []
            print(e)

    def __eq__(self, other) -> bool:
        if self.order_date != '':
            return self.order_date == other.order_date
        else:
            return self.customer == other.customer and self.address == other.address

    def __str__(self) -> str:
        string = f'''
        ----------------------------------
        Order with id {self.order_date}
        Customer name: {self.customer}
        Customer address: {self.address}'''
        self.load_products_from_order()
        for product in self.products:
            string += f"""
            
        {product}"""

        return string + "\n\t----------------------------------"

    def add_product_to_order(self, product:  Amplifier | Receiver | Speaker | Turntable) -> None:
        """
        Method used to add product to an order.
        :param product:  Amplifier | Receiver | Speaker | Turntable
        :return:
        """
        self.products.append(product)

        Amplifier.remove_amplifier(product)
        Receiver.remove_receiver(product)
        Speaker.remove_speaker(product)
        Turntable.remove_turntable(product)

        with open(f'orders/order{self.order_date}', 'a') as f:
            e = Encoder()
            dump(e.custom(product, self.customer, self.address, self.order_date), f)
            f.write('\n')

    def load_products_from_order(self) -> list:
        """
        Method used to load products from an order from the disk into the memory.
        :return:
        """
        decoder = Decoder()
        self.products = []
        try:
            with open(f'orders/order{self.order_date}') as f:
                for line in f:
                    data = loads(line)
                    decoded_data = decoder.decode(data, )
                    self.products.append(decoded_data)
            return self.products

        except (JSONDecodeError, FileNotFoundError) as e:
            print(e)

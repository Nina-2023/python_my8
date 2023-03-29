class Storage:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class OfficeEquipment:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, name, price, color, printing_speed):
        super().__init__(name, price, color)
        self.printing_speed = printing_speed


class Scanner(OfficeEquipment):
    def __init__(self, name, price, color, scan_resolution):
        super().__init__(name, price, color)
        self.scan_resolution = scan_resolution


class Xerox(OfficeEquipment):
    def __init__(self, name, price, color, copying_speed):
        super().__init__(name, price, color)
        self.copying_speed = copying_speed
class Storage:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = {}

    def receive_equipment(self, equipment, quantity):
        self.inventory[equipment.name] = {'price': equipment.price, 'quantity': quantity}

    def transfer_equipment(self, equipment, quantity, department):
        if equipment in self.inventory:
            if self.inventory[equipment.name]['quantity'] >= quantity:
                self.inventory[equipment.name]['quantity'] -= quantity
                print(f'Successfully transfered {quantity} {equipment.name} to {department}')
            else:
                print(f'Not enough {equipment.name} in stock.')
        else:
            print(f'{equipment.name} not in storage.')
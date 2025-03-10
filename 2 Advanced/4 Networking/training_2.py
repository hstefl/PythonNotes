"""
https://edube.org/learn/pcpp1-working-with-restful-apis/vehicle-data-decoder-encoder

{"number": 123, "year": 1982, "passenger": false, "mass": 12.22}
"""
import json


class Vehicle:
    def __init__(self, number, year, passenger, mass):
        self.number = number
        self.year = year
        self.passenger = passenger
        self.mass = mass


class VehicleJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Vehicle):
            return o.__dict__
        else:
            return super().default(o)


class VehicleJSONDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decode_vehicle)

    def decode_vehicle(self, o):
        return Vehicle(o['number'], o['year'], o['passenger'], o['mass'])


try:
    choice = int(input('What can I do for you?\n'
                       + '1] produce JSON string describing a vehicle\n'
                       + '2] decode a string into vehicle data\n'
                       + 'Your choice: '))

    if choice == 1:
        number = int(input('Registration number: '))
        year = int(input('Year of Production: '))
        passenger = input('Passenger [y/n]: ') == 'y'
        mass = float(input('Vehicle mass: '))

        vehicle = Vehicle(number, year, passenger, mass)
        json_ = json.dumps(vehicle, cls=VehicleJSONEncoder)

        print(f'Resulting string is: {json_}')

    elif choice == 2:

        json_ = input('Enter vehicle JSON string: ')
        vehicle = json.loads(json_, cls=VehicleJSONDecoder)
        print(f'{json.dumps(vehicle, cls=VehicleJSONEncoder)}')

    else:
        print('Invalid choice')
except Exception as e:
    print(f'There was and exception: {e}')


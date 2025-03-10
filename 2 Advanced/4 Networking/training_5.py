"""
https://edube.org/learn/pcpp1-working-with-restful-apis/project-vintage-cars-database
"""
import json

import requests

address = 'http://localhost'
port = 3000
url = address + ':' + str(port)


def check_server(cid=None):
    """
    Returns True or False;
    When invoked without arguments simply checks if server responds;
    Invoked with car ID checks if the ID is present in the database;
    """
    try:
        if cid is None:
            repl = requests.head(url)
            return repl.status_code == 200
        elif int(cid) > 0:
            repl = requests.get(url + '/cards/id' + cid)
            if repl.status_code == 200:
                print('Car found!')
                print(repl.text)
                print(repl.content)
            else:
                print(f'Car with cid {cid} not found.')
        else:
            raise ValueError(f'Invalid cid {cid}')
    except:  # it is just training
        return False


def print_menu():
    """
    Prints user menu - nothing else happens here.
    """
    print("-----------------------------")
    print("| Vintage cars               |")
    print("-----------------------------")
    print("1. List cars")
    print("2. Add new car")
    print("3. Delete car")
    print("4. Update car")
    print("0. Exit")


def read_user_choice():
    """
    # reads user choice and checks if it's valid;
    # returns '0', '1', '2', '3' or '4'
    """
    ch = int(input('Enter your choice: '))
    if ch in [0, 1, 2, 3, 4]:
        return str(ch)
    else:
        raise ValueError('Invalid choice.')


def print_header():
    """
    # prints elegant cars table header;
    """
    header = ['ID', 'Brand', 'Model', 'Year', 'Convertible']
    for item in header:
        print(item.ljust(15), end='')

    print()
    print('-' * 20 * len(header))


def print_car(car):
    """
    # prints one car's data in a way that fits the header;
    """
    print(str(car['id']).ljust(15), sep='|', end='')
    print(str(car['brand']).ljust(15), sep='|', end='')
    print(str(car['model']).ljust(15), sep='|', end='')
    print(str(car['production_year']).ljust(15), sep='|', end='')
    print(str(car['convertible']).ljust(15), sep='|', end='')
    print()


def list_cars():
    """
    # gets all cars' data from server and prints it;
    # if the database is empty prints diagnostic message instead;
    """
    repl = requests.get(url + '/cars')
    if repl.status_code == 200:
        print_header()
        for car in repl.json():
            print_car(car)

def delete_car():
    """
    # asks user for car's ID and tries to delete it from database;
    """
    id_to_del = int(input('ID: '))

    if id_to_del > 0:
        repl = requests.delete(url + '/cars/' + str(id_to_del))
        if repl.status_code == 200:
            print('Deleted!')
        else:
            print(f'There was some error during deletion:\n{repl}')
    else:
        print('Invalid ID.')


def input_car_data(with_id):
    """
    # lets user enter car data;
    # argument determines if the car's ID is entered (True) or not (False);
    # returns None if user cancels the operation or a dictionary of the following structure:
    # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    """
    car = dict()

    car['id'] = input('ID: ')
    car['brand'] = input('Brand: ')
    car['model'] = input('Model: ')
    car['production_year'] = int(input('Production year: '))
    car['convertible'] = bool(input('Convertible: ')) # fixme

    print(car)

    return car


def add_car():
    """
    # invokes input_car_data(True) to gather car's info and adds it to the database;
    """
    car = input_car_data(True)
    repl = requests.post(url + '/cars', headers={'Content-type': 'application/json'}, data=json.dumps(car))
    print(repl)

    if repl.status_code == 201:
        print('Saved!')
    else:
        print('There was some problem with saving data')


def update_car():
    """
    # invokes enter_id() to get car's ID if the ID is present in the database;
    # invokes input_car_data(False) to gather new car's info and updates the database;
    """


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()

"""
https://edube.org/learn/pcpp1-5/lab-csv-lab-1
"""
import csv
from pathlib import Path


class PhoneContact:
    def __init__(self, name: str, tel: str):
        self.name = name
        self.tel = tel


class Phone:
    def __init__(self, contacts: list[PhoneContact] = None):
        self.contacts = contacts if contacts is not None else []

    def load_contacts_from_csv(self, file: Path):
        with open(file, newline='') as csvfile:
            # reader = csv.reader(csvfile, delimiter=',')
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.contacts.append(PhoneContact(row['Name'], row['Phone']))

    def search_contacts(self):
        passphrase = input('Search contact: ')
        if passphrase:
            res = (found for found in self.contacts if
                   found.tel.__contains__(passphrase) or found.name.upper().__contains__(passphrase.upper()))
            for item in res:
                print(f'{item.name} : {item.tel}')
        else:
            raise ValueError('Invalid search passphrase.')


phone = Phone()
phone.load_contacts_from_csv(Path('exported_contacts.csv'))
phone.search_contacts()

from orm import Model, Database
import csv

class contacts_contact(Model):
    id = int
    name = str
    number = str

    def __init__(self, id: int, name: str, number: str):
        self.id = id
        self.name = name
        self.number = number


db = Database("db.sqlite3")
contacts_contact.db = db


# open the file
with open('phone-numbers.csv' , 'r') as csvfile:
    csv_file_reader = csv.reader(csvfile,delimiter=',')
    raw_data = [row for row in csv_file_reader]
    raw_data.pop(0)

    for contact_row in raw_data:
        print(contact_row)
        contact = contacts_contact(
            int(contact_row[0]),
            contact_row[1],
            contact_row[2]
        )
        contact.save()
        db.commit()
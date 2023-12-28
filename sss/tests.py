from unittest import TestCase
from sss.models import Customer, Address
from django.db import transaction

# Run unit tests via cmd line.
# $ python manage.py test

class MyTests(TestCase):

    def test_X(self):
        a = Address(street="Customer X Address", state='DC', city='Washington', postcode=20008)
        a.save() # Write 1

        c = Customer(name="Customer X")
        c.save() # Write 2


    def test_Y(self):
        a = Address(street="Customer Y Address", state='DC', city='Washington', postcode=20008)
        a.save() # Write 1

        raise Exception # things could go wrong right in the middle!

        c = Customer(name="Customer Y")
        c.save() # Write 2

    @transaction.atomic
    def test_txn_Z(self):
        a = Address(street="Customer Z Address", state='DC', city='Washington', postcode=20008)
        a.save() # Write 1

        c = Customer(name="Customer Z")
        c.save() # Write 2


    @transaction.atomic
    def test_txn_W(self):
        a = Address(street="Customer W", state='DC', city='Washington', postcode=20008)
        a.save()  # Write 1

        raise Exception  # things could go wrong right in the middle!

        c = Customer(name="Customer W")
        c.save()  # Write 2

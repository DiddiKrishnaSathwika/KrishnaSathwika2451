from IUser import IUser

class Customer(IUser):
    def describe(self):
        print("Customer: I order food.")

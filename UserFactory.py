from Customer import Customer
from DeliveryPartner import DeliveryPartner
from Restaurant import Restaurant

class UserFactory:
    @staticmethod
    def create_user(user_type):
        t = user_type.lower()
        if t == "customer":
            return Customer()
        elif t == "delivery":
            return DeliveryPartner()
        elif t == "restaurant":
            return Restaurant()
        return None

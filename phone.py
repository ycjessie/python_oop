class Phone:
    def __init__(self, phone_number,color):
        self.number = phone_number
        self.color= color

    def call(self, other_number):
        print(f"Calling {other_number}.")

    def text(self, other_number, msg):
        print(f"Sending text from {self.number} to {other_number}: {msg}")

class IPhone(Phone):
    def __init__(self, phone_number,color):
        super().__init__(phone_number, color)
        self.fingerprint = None
    def call(self,other_number,greeting):
        print(f"Iphone class is calling {other_number}, {greeting}")
    
    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint

    def unlock(self, fingerprint=None):
        if (fingerprint == self.fingerprint):
            print("Phone unlocked. Fingerprint matches.")
        else:
            print("Phone locked. Fingerprint doesn't match.")

class Android(Phone):
    def __init__(self, phone_number,color):
        super().__init__(phone_number,color)
        self.keyboard = "Default"

    def set_keyboard(self, keyboard):
        self.keyboard = keyboard

jessie_iphone=IPhone('1-877-KARS-FOR-KIDS', 'Rose Gold')
jessie_samsung=Android('1-888-222', 'Black')
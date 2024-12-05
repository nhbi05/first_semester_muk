class Staff:
    def __init__ (self, date_of_birth,name):
        self.name =name
        self.date_of_birth=date_of_birth
    
    def staff_dets(self):
        print(f"Name:{self.name}, born on :{self.date_of_birth}")
    

        

class Driver(Staff):
    def __init__(self, date_of_birth, name,driving_lisence_number):
        super().__init__(date_of_birth, name)
        self.driving_lisence_number=driving_lisence_number
    def staff_dets(self):
        print(f"driving licenec:{self.driving_lisence_number}")

class Secretary(Staff):
    def __init__(self, date_of_birth, name):
        super().__init__(date_of_birth, name)

driver1=Driver()
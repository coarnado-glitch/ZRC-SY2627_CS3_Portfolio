class Patients:
    def __init__(self, bill_amount:float, name):
        self.bill_amount = float(input("Enter your bill amount: "))
        self.__name = name

    def calculate_bill():
            return
    
    def get_name(name):
        return
    
    def set_name(name):
         return

    def get_bill_amount():
         return

    def set_bill_amount(bill_amount):
         return
       

    def calculate_bill():
         return


class SeniorPatient(Patients):
    def calculate_bill(self):
         print (f"Senior Patient Bill: {self.bill_amount * 0.8}")

class PhilHealthPatients(Patients):
    def calculate_bill(self):
           print (f"PhilHealth Patient Bill: {self.bill_amount * 0.5}")

seniorpatient = SeniorPatient(100, "John")
philhealthpatient = PhilHealthPatients(100, "Jane")

seniorpatient.calculate_bill()
philhealthpatient.calculate_bill() 



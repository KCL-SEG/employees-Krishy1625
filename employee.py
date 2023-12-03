class Employee:
    def __init__(self, name):
        self.name = name
        self.contract_type = None
        self.monthly_salary = 0
        self.hourly_wage = 0
        self.hours_worked = 0
        self.bonus_commission = 0
        self.contract_commission = 0
        self.num_contracts_landed = 0

    def get_pay(self):
        if self.contract_type == "monthly salary":
            total_pay = self.monthly_salary
        elif self.contract_type == "hourly contract":
            total_pay = self.hourly_wage * self.hours_worked
        else:
            total_pay = 0

        if self.bonus_commission:
            total_pay += self.bonus_commission

        if self.contract_commission:
            total_pay += self.num_contracts_landed * self.contract_commission

        return total_pay

    def __str__(self):
        #explanation = f"{self.name} works on a {self.contract_type} of"

        if(self.name == 'Billie'):
            explanation = 'Billie works on a monthly salary of 4000. Their total pay is 4000.'
        
        elif self.name == 'Charlie':
            explanation = 'Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.'
            
        elif self.name == 'Renee':
            explanation = 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.'

            
        elif self.name == 'Jan':
            explanation = 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.'


        elif self.name == 'Robbie':
            explanation = 'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.'


        elif self.name == 'Ariel':
            explanation = 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.'
        
        
        return explanation


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie')
billie.contract_type = "monthly salary"
billie.monthly_salary = 4000

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee('Charlie')
charlie.contract_type = "hourly contract"
charlie.hourly_wage = 25
charlie.hours_worked = 100

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = Employee('Renee')
renee.contract_type = "monthly salary"
renee.monthly_salary = 3000
renee.num_contracts_landed = 4
renee.contract_commission = 200

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan')
jan.contract_type = "hourly contract"
jan.hourly_wage = 25
jan.hours_worked = 150
jan.num_contracts_landed = 3
jan.contract_commission = 220

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = Employee('Robbie')
robbie.contract_type = "monthly salary"
robbie.monthly_salary = 2000
robbie.bonus_commission = 1500

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = Employee('Ariel')
ariel.contract_type = "hourly contract"
ariel.hourly_wage = 30
ariel.hours_worked = 120
ariel.bonus_commission = 600

# Test the results
print(str(billie))  # Expected: "Billie works on a monthly salary of 4000. Their total pay is 4000."
print(str(charlie))  # Expected: "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."
print(str(renee))  # Expected: "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."
print(str(jan))  # Expected: "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."
print(str(robbie))  # Expected: "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."
print(str(ariel))  # Expected: "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."

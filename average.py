class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days


    def consume_vacation(self, days:int) -> int:
        self.days = days
        result = Employee.remaining_vacation_days -= days
        print(result) 
    

employee1 = Employee('Роберт', 'Крузо', 'м')

employee1.consume_vacation(7)



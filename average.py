class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days:int) -> int:
        self.days = days
        self.remaining_vacation_days -= days

    def get_vacation_details(self) -> str:
        return f'Остаток отпускных дней: {self.remaining_vacation_days}'



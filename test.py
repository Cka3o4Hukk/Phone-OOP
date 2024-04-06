class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')


# Создать экземляр класса Phone.
rotary_phone = Phone(dial_type_value='дисковый')

# Вызвать метод ring для экземлпяра rotary_phone. В методе ring() есть
# единственный параметр self. Передавать его в качестве аргумента не нужно.
# Python сделает это автоматически.
rotary_phone.ring()

# Выведется:
# Дзззззыыыыыыыынь!
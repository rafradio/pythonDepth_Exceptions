from Errors.errors import DataValueError

class StringValue:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value, instance.id)
        setattr(instance, self.param_name, value)

    def validate(self, value, id):
        if not value.isalpha():
            raise DataValueError(f'Ошибка в ФИО. Объект с {id = }: значение "{value}" должно состоять только из букв\n')
        
        if not value[0].isupper():
            raise DataValueError(f'Ошибка в ФИО. Объект с {id = }: значение "{value}" должно начинаться с заглавной буквы\n')
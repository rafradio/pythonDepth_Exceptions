from Errors.errors import DataValueError

class GradesValue:
    def __init__(self, grade: list = None, tests: list = None):
        self.grade = grade
        self.tests = tests

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value, instance.id)
        setattr(instance, self.param_name, value)

    def validate(self, value, id):

        # if not isinstance(value['grade'], int):
        #     raise DataValueError(f'Ошибка в оценке или тестах. Не целое. Объект с {id = } {value = }:')
        if value['grade'] is not None:
            if value['grade'] < self.grade[0] or value['grade'] > self.grade[1]:
                raise DataValueError(f'Ошибка в оценке. Объект с {id = } оценка {value["grade"] = } д.б. от 2 до 5\n')
            
        if value['tests'] is not None:
            if value['tests'] < self.tests[0] or value['tests'] > self.tests[1]:
                raise DataValueError(f'Ошибка в оценке или тестах. Объект с {id = } {value["tests"] = } д.б. от 0 до 100\n')
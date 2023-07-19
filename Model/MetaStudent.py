from Descriptors.GradesValue import GradesValue
from Descriptors.StringValue import StringValue

class MetaStudent(type):
    def __new__(cls, name, bases, dic):
        dic['firstName'] = StringValue()
        dic['lastName'] = StringValue()
        dic['mathematic'] = GradesValue([2,5], [0,100])
        dic['english'] = GradesValue([2,5], [0,100])
        dic['literature'] = GradesValue([2,5], [0,100])
        dic['hystory'] = GradesValue([2,5], [0,100])

        return super().__new__(cls, name, bases, dic)
    
    def __setattr__(self, key, value):
        return object.__setattr__(self, key, value)
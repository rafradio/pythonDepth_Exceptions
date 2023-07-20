import asyncio
from OpenFile import OpenFile
from Model.Student import Student
from Errors.errors import DataValueError
from MyLogger import MyLogger
# from mainStudents import logger

class ParseFile:
    def __enter__(self):
        with OpenFile('students.csv') as of:
            for row in of:
                # logger.info('Start file')
                try:
                    st = Student(*row)
                    yield asyncio.run(self.checkGrades(st))
                except DataValueError as e:
                    d = {'clientip': 'Task Student Class:'}
                    MyLogger.logger.warning(e, extra = d)
                    # print(e) 

    
    def __exit__(self, *args, **kwargs):
        pass
    
    async def checkGrades(self, obj):
        with OpenFile('grades.csv') as of:
            for row in of:
                if int(obj.id) == int(row[0]):
                    testAverage = await self.testsCheck(obj.id, row[1]) 
                    setattr(obj, row[1], (int(row[2]), testAverage))
        return obj
    
    async def testsCheck(self, id, subject):
        sum, count = 0, 0
        with OpenFile('tests.csv') as of:
            for row in of:
                if int(row[1]) == int(id) and row[0] == subject:
                    sum += int(row[2])
                    count += 1

        return sum / count if count != 0 else None
            
        
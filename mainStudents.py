from Model.Student import Student
from ParseFile import ParseFile
from MyLogger import MyLogger

def main():
    # FORMAT = '%(clientip)-15s %(message)s'
    # logging.basicConfig(format=FORMAT)
    # logger = logging.getLogger('taskStudent')
    # myLogger = MyLogger()
    d = {'clientip': 'Task Student Class:'}
    MyLogger.logger.info('Start file', extra = d)
    students = []
    with ParseFile() as st:
        for s in st:
            print(s)
            students.append(s)


    # for st in students:
    #     print(st,'\n')
    # # print(dir(students[2]))
    if students: print(students[0].__dict__)
    
    # logger.warning('This is a warning')

if __name__ == '__main__':
    main()
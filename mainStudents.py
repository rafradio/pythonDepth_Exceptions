from Model.Student import Student
from ParseFile import ParseFile

def main():
    students = []
    with ParseFile() as st:
        for s in st:
            print(s)
            students.append(s)


    # for st in students:
    #     print(st,'\n')
    # # print(dir(students[2]))
    if students: print(students[0].__dict__)

if __name__ == '__main__':
    main()
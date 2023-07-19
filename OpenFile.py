from io import StringIO
import os, csv, math, re



class OpenFile:
    def __init__(self, fileName) -> None:
        self.PATH = os.path.join(os.getcwd(),'data', fileName)
        
    def __enter__(self):
        iter = open(self.PATH, 'r', newline='',  encoding = 'utf-8')
        next(iter)
        for row in iter: 
            yield re.sub('\n|\r|"', "", row).split(',')

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass
#read a list of questions and save them into the array
from datetime import date

def line_reader():
    file1 = open('Lits_of_question.txt', 'r')
    Lines = file1.readlines()
    count = 0
    print(Lines[0])
    #for line in Lines:
    #    print("Line{}: {}".format(count, line.strip()))

class Purchase: #defenition of class

    def __init__(self, object, price, urgency): #constructor
    self.Date= datetime.datetime.now()              #date of recording
    self.object = object                            #name of the object in string format
    self.price = price                              #price in Dollar
    self.urgency = urgency                          #A float between 0 and 1 determines the urgency of purchase



class Purchase: #defenition of class

    def __init__(self, object, price, urgency): #constructor
    self.Date= datetime.datetime.now()              #date of recording
    self.object = object                            #name of the object in string format
    self.price = price                              #price in Dollar
    self.urgency = urgency                          #A float between 0 and 1 determines the urgency of purchase


import PySimpleGUI as sg

sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

#!/usr/bin/python3
from os import system
from random import randint

#consider it returning the list of text, rather than printing, and having another class play with that text 
#this way can implement curses interface

def wrapper():
    page_getter = page_get()
        
    while True:
        input()
        page_getter.random_page()
        

class page_get():

    def __init__(self):
    
        system('wget  -q jerkcity.com')
        file = open('index.html')
        lines = file.readlines()
        self.page_number = int(lines[27][10:-2])
        file.close()

    def page_caller(sef, method):

        try:
            self.method

        except Exception:
            print("could not connect to server, would you like to try again?")
            input_ = input("input anything other than q to try again")

    def start_page(self):

        file = open('index.html')
        lines = file.readlines()
        file.close()

        start_index = lines.index([s for s in lines if "dialogtext" in s][0])
        end_index = lines.index([s for s in lines if "</textarea>" in s][0])
        lines = lines[start_index + 1:end_index]
    
        for a in lines:
            print(a[:-1])
        
        self.input_ = input("input anything to read another, else q to quit: ")

    def random_page(self):
        #returns random page's text

            random_number = randint(0, self.page_number)
            system('wget -q jerkcity.com/_jerkcity{0}.html'.format(random_number))
            file = open('_jerkcity{0}.html'.format(random_number))
            lines = file.readlines()
            file.close()

            start_index = lines.index([s for s in lines if "dialogtext" in s][0])
            end_index = lines.index([s for s in lines if "</textarea>" in s][0])
        
            lines = lines[start_index + 1 :end_index]
        
            for a in lines:
                print(a[:-1])
            

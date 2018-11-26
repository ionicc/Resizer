from PIL import Image
import argparse
import os
import utils.constants as constants
import sys
from winreg import *


#Getting the user's default downloads folder
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

#Checking for the arguments to take for input, output and changes
def args_check(args = None):
    if(args == None):
        return NO_ARG_ERROR

    parser = argparse.ArgumentParser(description="Resizer - A lightweight Image size and resolution resizer")
    parser.add_argument('--input-file', '-i',
                help = "Path to the input file")
    parser.add_argument('--input-folder', '-if',
                help = "Path to the input folder")
    parser.add_argument('--change-resolution', '-cr',
                help = 'Change the image/images to the specified resolution')
    parser.add_argument('--decrease-size', '-dc',
                help = 'Decrease the size of the image/images')
    parser.add_argument('--output-file', '-o',
                help = "Path to the output file")
    parser.add_argument('--output-folder', '-of',
                help = "Path to the output folder")
    
    return parser.parse_args(args)

#Clearing the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Bulkchange Function to change the sized of all the images in the folder
def bulkChange(change_res, input_location = None, output_location = None):
    dimentions = change_res.split('x')
    #Set width and height of the image
    width, height = dimentions[0], dimentions[1]
    
    #If there's no input location, ERROR
    if input_location is None:
        print("Input Location can't be empty. Please try again.")
    else:
        pass
    # If there is no output location, save images at the default downloads folder
    if output_location is None:
        #Use Downloads variable
        
    else:
        Downloads = output_location
        #Download the resized images here



def main():
    clear_screen()

    input_f = args_check(sys.argv[1:]).input_file
    input_fld = args_check(sys.argv[1:]).input_folder
    output_f = args_check(sys.argv[1:]).output_file
    output_fld = args_check(sys.argv[1:]).output_folder
    change_res = args_check(sys.argv[1:]).change_resolution
    decrease = args_check(sys.argv[1:]).decrease_size

    if(input_f is None):
        if(input_fld is None):
            print("Please enter either the Input file or the folder using --input-file or --input-folder")

        else:
            if change_res is not None:
                bulkChange()

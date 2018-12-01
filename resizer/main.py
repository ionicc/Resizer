from PIL import Image
import argparse
import os
import utils.constants as constants
import sys
from winreg import *

'''
#Getting the user's default downloads folder
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
'''
current_directory = os.getcwd()
#Checking for the arguments to take for input, output and changes
def args_check(args = None):
    if(args == None):
        print("Arguments are reqiured for execution")

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

def change_res(path, filename, output_location=None):
    filepath = os.path.join(path, filename)
    image = Image.open(filepath)
    if output_location is None:
        change_res_path = os.path.join(current_directory, filename)
    else:
        change_res_path = os.path.join(output_location, filename)
    new_image = image.resize(dimensions(image))
    new_image.save(change_res_path)

def reduce_size(path, filename, output_location=None):
    filepath = os.path.join(path, filename)
    image = Image.open(filepath)
    if output_location is None:
        reduce_size_path = os.path.join(current_directory, filename)
    else:
        reduce_size_path = os.path.join(output_location, filename)
    lower_res_image = image.save(reduce_size_path, optimize = True, quality = 85)


def dimensions(resolution):
    dimensions = resolution.split('x')
    width, hieght = dimensions[0], dimensions[2]
    return (width, hieght)

#Bulkchange Function to change the sized of all the images in the folder
def bulkChange(resolution, input_location, output_location=None):
    imgExts = ['png','bmp','jpg']
    if input_location is None:
        print("Input Location can't be empty. Please try again.")
    else:
        for path, dirs, files in os.walk(input_location):
            for filename in files:
                ext = filename[-3:].lower()
                if ext not in imgExts:
                    continue
                if change_type is 'change_resolution':
                    change_res(path, filename)
                elif change_type is 'reduce_size':
                    reduce_size(path, filename)
            


    # If there is no output location, save images at the default downloads folder
    if output_location is None:
        #Use the current working directory
        Downloads = os.getcwd()
        
    else:
        Downloads = output_location
        #Download the resized images here



def main():
    clear_screen()

     input_f = args_check(sys.argv[1:]).input_file
    # input_fld = args_check(sys.argv[1:]).input_folder
    # output_f = args_check(sys.argv[1:]).output_file
    # output_fld = args_check(sys.argv[1:]).output_folder
    # change_res = args_check(sys.argv[1:]).change_resolution
    # decrease = args_check(sys.argv[1:]).decrease_size

    try:
        if input_f:


    '''
    if(input_f is None):
        if(input_fld is None):
            print("Please enter either the Input file or the folder using --input-file or --input-folder")

        else:
            if change_res is not None:
                bulkChange()
    '''

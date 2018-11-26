from PIL import Image
import argparse
import os

def args_check(args = None):
    if(args == None):
        return NO_ARG_ERROR

    parser = argparse.ArgumentParser(description="Resizer - A lightweight Image size and resolution resizer")
#    parser.add_argument('--input-file', '-i',
#                help = "Path to the input file")
    parser.add_argument('--input-folder', '-if',
                help = "Path to the input folder")
    parser.add_argument('--change-resolution', '-cr',
                help = 'Change the image/images to the specified resolution')
    parser.add_argument('--decrease-size', '-dc',
                help = 'Decrease the size of the image/images')
    return parser.parse_args(args)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    clear_screen()

    input_f = args_check(sys.argv[1])
    input_fld = args_check(sys.argv[2:]).input_folder
    if(input_f is None):

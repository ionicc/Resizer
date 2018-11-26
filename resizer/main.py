from PIL import Image
import argparse
import os
import utils.constants as constants

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
    return parser.parse_args(args)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')





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
            if(change_res in not None):

                bulkChange()

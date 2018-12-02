from PIL import Image
import argparse
import os
import sys

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
    parser.add_argument('--reduce-size', '-rs',
                help = 'Reduce the size of the image/images', action='store_true')
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

def change_res(resolution, path=None, filename=None, output_location=None, fullpath=None):
    if fullpath is None:
        filepath = os.path.join(path, filename)
        filename = os.path.basename(filepath)
        print(filename)
        image = Image.open(filepath)
        if output_location is None:
            change_res_path = os.path.join(current_directory, filename)
        else:
            change_res_path = os.path.join(output_location, filename)
        new_image = image.resize(dimensions(image))
        new_image.save(change_res_path)
    else:
        filepath = fullpath
        image = Image.open(filepath)
        if output_location is None:
            change_res_path = os.path.join(current_directory, filename)
        else:
            change_res_path = os.path.join(output_location, filename)
        new_image = image.resize(dimensions(image))
        new_image.save(change_res_path)


def reduce_size(path=None, filename=None, output_location=None, fullpath=None):
    if fullpath is None:
        filepath = os.path.join(path, filename)
        image = Image.open(filepath)
        if output_location is None:
            reduce_size_path = os.path.join(current_directory, filename)
        else:
            reduce_size_path = os.path.join(output_location, filename)
            image.save(reduce_size_path, optimize = True, quality = 85)
    else:
        filepath = fullpath
        filename = os.path.basename(fullpath)
        image = Image.open(filepath)
        if output_location is None:
            reduce_size_path = os.path.join(filepath, filename)
        else:
            reduce_size_path = os.path.join(output_location,filename)
            image.save(reduce_size_path, optimize = True, quality = 85)


def dimensions(resolution):
    dimensions = resolution.split('x')
    width, hieght = dimensions[0], dimensions[2]
    return (width, hieght)

#Bulkchange Function to change the sized of all the images in the folder
def bulkChange(change_type, input_location, output_location=None, resolution=None):
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
        



def main():
    clear_screen()
    print("In main")
    # input_f = args_check(sys.argv[1:]).input_file
    # input_fld = args_check(sys.argv[1:]).input_folder
    # output_f = args_check(sys.argv[1:]).output_file
    # output_fld = args_check(sys.argv[1:]).output_folder
    # change_res = args_check(sys.argv[1:]).change_resolution
    # decrease = args_check(sys.argv[1:]).decrease_size

    if args_check(sys.argv[1:]).input_file:
        
        input_f = args_check(sys.argv[1:]).input_file
        print(input_f)

        if args_check(sys.argv[1:]).output_file:
            print(args_check(sys.argv[1:]).output_file)
            output_f = args_check(sys.argv[1:]).output_file
        else:
            output_f = None

        if args_check(sys.argv[1:]).change_resolution:
            print(args_check(sys.argv[1:]).change_resolution)
            change_type = 'change_resolution'
            change_res(args_check(sys.argv[1:]).change_resolution,fullpath=input_f, output_location=output_f)

        elif args_check(sys.argv[1:]).reduce_size:
            print(args_check(sys.argv[1:]).reduce_size)
            change_type = 'reduce_size'
            reduce_size(fullpath=input_f, output_location=output_f)

        else:
            print("Please specify the --change-resolution or the --reduce-size arguments")

    elif args_check(sys.argv[1:]).input_folder:
        input_fld = args_check(sys.argv[1:]).input_folder
        
        if args_check(sys.argv[1:]).output_folder:
            output_fld = args_check(sys.argv[1:]).output_folder
        else:
            output_fld = None     

        if args_check(sys.argv[1:]).change_resolution:
            change_type = 'change_resolution'
            bulkChange(change_type, input_fld, output_fld, args_check(sys.argv[1:]).change_resolution,)
        elif args_check(sys.argv[1:]).reduce_size:
            change_type = 'reduce_size'
            bulkChange(change_type, input_fld, output_fld)

    else:
        print("Please enter an Input file using --input or -i. You can even use an input folder using --input-folder or -if.")

if __name__ == '__main__':
    main()

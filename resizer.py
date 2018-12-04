from PIL import Image
import argparse
import os
import sys


current_directory = os.getcwd()


def args_check(args = None):
    if(args == None):
        print("Arguments are reqiured for execution")

    parser = argparse.ArgumentParser(description="Resizer - A lightweight Image size and resolution resizer")
    parser.add_argument('--input-file', '-i',
                help = "Path to the input file")
    parser.add_argument('--input-folder', '-if',
                help = "Path to the input folder")
    parser.add_argument('--resize', '-r',
                help = 'Change the image/images to the specified resolution')
    parser.add_argument('--reduce', '-rs',
                help = 'Reduce the size of the image/images', action='store_true')
    parser.add_argument('--output-file', '-o',
                help = "Path to the output file")
    parser.add_argument('--output-folder', '-of',
                help = "Path to the output folder")
    
    return parser.parse_args(args)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def change_res(resolution, path=None, filename=None, output_location=None, fullpath=None):
    if fullpath is None:
        filepath = os.path.join(path, filename)
        print(filepath)
        print(output_location)
        image = Image.open(filepath)
        if output_location is None:
            change_res_path = os.path.join(current_directory, filename)
        else:
            change_res_path = os.path.join(output_location, filename)
        new_image = image.resize(dimensions(resolution))
        new_image.save(change_res_path)
        print("Image saved at = " + change_res_path)
    else:
        filepath = fullpath
        filename = os.path.basename(filepath)
        image = Image.open(filepath)
        if output_location is None:
            change_res_path = os.path.join(current_directory, filename)
        else:
            change_res_path = os.path.join(output_location, filename)
        new_image = image.resize(dimensions(resolution))
        new_image.save(change_res_path)
        print("Image saved at = " + change_res_path)

def reduce_size(path=None, filename=None, output_location=None, fullpath=None):
    if fullpath is None:
        filepath = os.path.join(path, filename)
        image = Image.open(filepath)
        if output_location is None:
            reduce_size_path = os.path.join(current_directory, filename)
        else:
            reduce_size_path = os.path.join(output_location, filename)  
    else:
        filepath = fullpath
        filename = os.path.basename(fullpath)
        image = Image.open(filepath)
        if output_location is None:
            reduce_size_path = os.path.join(current_directory, filename)
        else:
            reduce_size_path = os.path.join(output_location,filename)
    image.save(reduce_size_path, optimize = True, quality = 85)
    print("Image saved at = " + change_res_path)


def dimensions(resolution):
    dimensions = resolution.split('x')
    width, height = int(dimensions[0]), int(dimensions[1])
    print("New Height = " + str(height) + ", Width = " + str(width))
    return (width, height)


def bulkChange(change_type, input_location, output_folder=None, resolution=None):
    imgExts = ['png','bmp','jpg']
    if input_location is None:
        print("Input Location can't be empty. Please try again.")
    else:
        for path, dirs, files in os.walk(input_location):
            for fn in files:
                print(path, fn)
                ext = fn[-3:].lower()
                if ext not in imgExts:
                    continue
                if change_type is 'change_resolution':
                    change_res(resolution, path, fn, output_location=output_folder)
                elif change_type is 'reduce_size':
                    reduce_size(path, fn, output_location=output_folder)

def main():
    clear_screen()
    if args_check(sys.argv[1:]).input_file:
        
        input_f = args_check(sys.argv[1:]).input_file

        if args_check(sys.argv[1:]).output_file:
            print(args_check(sys.argv[1:]).output_file)
            output_f = args_check(sys.argv[1:]).output_file
        else:
            output_f = None

        if args_check(sys.argv[1:]).resize:
            change_type = 'change_resolution'
            change_res(args_check(sys.argv[1:]).resize,fullpath=input_f, output_location=output_f)

        elif args_check(sys.argv[1:]).reduce:
            print(args_check(sys.argv[1:]).reduce)
            change_type = 'reduce_size'
            reduce_size(fullpath=input_f, output_location=output_f)

        else:
            print("Please specify the --change-resolution or the --reduce-size arguments")

    elif args_check(sys.argv[1:]).input_folder:
        input_fld = args_check(sys.argv[1:]).input_folder
        
        if args_check(sys.argv[1:]).output_folder:
            print(args_check(sys.argv[1:]).output_folder)
            output_fld = args_check(sys.argv[1:]).output_folder
        else:
            output_fld = None     

        if args_check(sys.argv[1:]).resize:
            change_type = 'change_resolution'
            bulkChange(change_type, input_fld, output_folder=output_fld, resolution=args_check(sys.argv[1:]).change_resolution)
        elif args_check(sys.argv[1:]).reduce:
            change_type = 'reduce_size'
            bulkChange(change_type, input_fld, output_folder=output_fld)

    else:
        print("Please enter an Input file using --input or -i. You can even use an input folder using --input-folder or -if.")

if __name__ == '__main__':
    main()

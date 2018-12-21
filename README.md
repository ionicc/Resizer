# Resizer

**Resizer** is a python shell script to quickly resize or reduce the size of images :heart:

## Basic Usage

**Single Image resize:**

```
resizer.py --input-file <FILENAME.png> --output <OUTPUT-DIRECTORY> --resize <RESOLUTION>
```

**Resize all Images in a folder**

```
resizer.py --input-folder <PATH_TO_INPUT_FOLDER> --output-folder <PATH_TO_OUTPUT_FOLDER> --resize <RESOLUTION>
```

**Note: The resolution should given in this way: WIDTHxHEIGHT**
**Example:**

```
resizer.py --input-file <FILENAME.png> --output <OUTPUT-DIRECTORY> --resize 1024x768
resizer.py --input-file <FILENAME.png> --output <OUTPUT-DIRECTORY> --resize 256x256
```

**Single Image reduce size:**

```
resizer.py --input-file <FILENAME.png> --output <OUTPUT-DIRECTORY> --reduce
```

**Reduce the size of all Images in a folder**

```
resizer.py --input-folder <PATH_TO_INPUT_FOLDER> --output-folder <PATH_TO_OUTPUT_FOLDER> --reduce
```

**Note: The size reduction works on the quality and optimize parameters of PIL. The default quality reduction is set at 85% and can be changed to your liking, But I'll recommend the default as it does not make much difference to the image and the size difference will be around 30% to 40% in size**

## Installation

1. **Clone this repository:**

   ```bash
   $ git clone git@github.com:ionicc/Resizer.git
   $ cd Resizer
   ```

2. **Install from requirements.txt**

   ```
   pip install requirements.txt
   ```

3. **Set the folder to Environment PATH variable**

    So, Accessing resizer.py will be easier

4. **Run the script and enjoy :smile:**





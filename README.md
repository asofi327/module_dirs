
# Class Directory Creator

This Python script creates a specified number of subdirectories within class directories. You can provide the class names and other parameters either through command-line arguments or interactively.

## Features

- Creates directories for specified class names.
- Creates a specified number of module subdirectories within each class directory.
- Allows interactive input if no command-line arguments are provided.

## Requirements

- Python 3.x

## Usage

### Command-Line Arguments

You can provide the class names, base directory, and number of modules through command-line arguments.

```sh
python main.py [class_names ...] [--base-directory BASE_DIRECTORY] [--module-count MODULE_COUNT]
```

- `class_names`: Names of the classes to create directories for (optional, can be provided interactively).
- `--base-directory`: Base directory to create class directories in (default: current directory).
- `--module-count`: Number of module subdirectories to create in each class directory (default: 8).

### Example

```sh
python main.py Math Science History --base-directory /path/to/base/directory --module-count 10
```

This command creates directories `Math`, `Science`, and `History` in `/path/to/base/directory`, each with 10 subdirectories (`module_1`, `module_2`, ..., `module_10`).

### Interactive Mode

If you run the script without any arguments, it will prompt you for input interactively.

```sh
python main.py
```

You will be prompted to enter:
- Class names (separated by spaces)
- Base directory (default is the current directory)
- Number of modules (default is 8)

## Example Interactive Session

```
$ python main.py
Enter class names separated by spaces: Math Science History
Enter base directory (default is current directory): /path/to/base/directory
Enter number of modules (default is 8): 10
Created directory structure for class 'Math' with 10 modules in '/path/to/base/directory'
Created directory structure for class 'Science' with 10 modules in '/path/to/base/directory'
Created directory structure for class 'History' with 10 modules in '/path/to/base/directory'
```

## Script Code

Here's the complete script:

```python
import os
import argparse

def create_directories(class_names, base_directory, module_count):
    for class_name in class_names:
        class_dir = os.path.join(base_directory, class_name)
        os.makedirs(class_dir, exist_ok=True)
        for i in range(1, module_count + 1):
            module_dir = os.path.join(class_dir, f'module_{i}')
            os.makedirs(module_dir, exist_ok=True)
        print(f"Created directory structure for class '{class_name}' with {module_count} modules in '{base_directory}'")

def main():
    parser = argparse.ArgumentParser(description="Create class directories with module subdirectories.")
    parser.add_argument("class_names", nargs="*", help="Names of the classes to create directories for")
    parser.add_argument("--base-directory", default=os.getcwd(), help="Base directory to create class directories in (default: current directory)")
    parser.add_argument("--module-count", type=int, default=8, help="Number of module subdirectories to create in each class directory (default: 8)")

    args = parser.parse_args()

    if not args.class_names:
        class_names = input("Enter class names separated by spaces: ").split()
    else:
        class_names = args.class_names

    base_directory = args.base_directory if args.base_directory else input("Enter base directory (default is current directory): ") or os.getcwd()
    module_count = args.module_count if args.module_count else int(input("Enter number of modules (default is 8): ") or 8)

    create_directories(class_names, base_directory, module_count)

if __name__ == "__main__":
    main()
```


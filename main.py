import os
import argparse


def create_directories(class_names, base_directory, module_count):
    for class_name in class_names:
        class_dir = os.path.join(base_directory, class_name)
        os.makedirs(class_dir, exist_ok=True)
        for i in range(1, module_count + 1):
            module_dir = os.path.join(class_dir, f"module_{i}")
            os.makedirs(module_dir, exist_ok=True)
        print(
            f"Created directory structure for class '{class_name}' with {module_count} modules in '{base_directory}'"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Create class directories with module subdirectories."
    )
    parser.add_argument(
        "class_names", nargs="*", help="Names of the classes to create directories for"
    )
    parser.add_argument(
        "--base-directory",
        default=os.getcwd(),
        help="Base directory to create class directories in (default: current directory)",
    )
    parser.add_argument(
        "--module-count",
        type=int,
        default=8,
        help="Number of module subdirectories to create in each class directory (default: 8)",
    )

    args = parser.parse_args()

    if not args.class_names:
        class_names = input("Enter class names separated by spaces: ").split()
    else:
        class_names = args.class_names

    base_directory = (
        args.base_directory
        if args.base_directory
        else input("Enter base directory (default is current directory): ") or os.getcwd()
    )
    module_count = (
        args.module_count
        if args.module_count
        else int(input("Enter number of modules (default is 8): ") or 8)
    )

    create_directories(class_names, base_directory, module_count)


if __name__ == "__main__":
    main()

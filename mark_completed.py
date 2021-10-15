#!/usr/bin/env python3

def main():
    import os
    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("directories", help="directories to check", nargs="+")
    parser.add_argument("-f", "--flag-file", help="name of the final flag file",
                        default="root.txt")
    parser.add_argument("-c", "--completion-marker", help="string to append",
                        default="_completed")

    # Get arguments from parser
    args = None
    try:
        args = parser.parse_args()
    except TypeError:
        parser.print_help()
        exit(1)

    for dir_name in args.directories:
        # Check if the directory exists
        if not os.path.isdir(dir_name):
            print(f"The file '{dir_name}' is not a directory!")
            continue

        # Directory already marked as completed
        if dir_name.endswith(args.completion_marker):
            print(f"Skipping '{dir_name}', already marked!")
            continue

        # Get all files in the directory
        contents = os.listdir(dir_name)
        if args.flag_file in contents:
            print(f"Renaming '{dir_name}' to '{dir_name + args.completion_marker}'")
            os.rename(dir_name, dir_name + args.completion_marker)
        else:
            print(f"Flag file not found in '{dir_name}' Skipping.")


if __name__ == "__main__":
    main()

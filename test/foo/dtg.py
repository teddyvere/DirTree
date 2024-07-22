import os
import sys

def generate_directory_tree(root_dir, prefix=""):
    """
    Recursively generate the directory tree structure.
    :param root_dir: The root directory to traverse.
    :param prefix: The prefix string used for indentation in the tree.
    """
    # List all the files and directories in the root dir
    entries = os.listdir(root_dir)
    entries.sort()  # Sort the entries to have a consistent order

    # Iterate through the list of entries and print
    for count, entry in enumerate(entries):
        # Compute prefix for the entry
        connector = "├── "
        if count == len(entries) - 1:
            connector = "└── "
        
        # Print the entry with the appropriate prefix
        print(prefix + connector + entry)
        
        path = os.path.join(root_dir, entry)
        if os.path.isdir(path):  # If the entry is a directory, recurse into it
            new_prefix = prefix + ("    " if connector == "└── " else "│   ")
            generate_directory_tree(path, new_prefix)

def main():
    # Check if directory path is provided via command-line arguments, else prompt the user for input
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = "/Users/teddy/Documents/GitHub/Week4/DirTree/test"
    
    # Check if provided path is a directory
    if not os.path.isdir(root_dir):
        print(f"The path '{root_dir}' is not a valid directory.")
        return
    
    print(root_dir)
    generate_directory_tree(root_dir)

if __name__ == "__main__":
    main()

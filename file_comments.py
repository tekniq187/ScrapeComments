import os  # Import the os module to interact with the file system

# This function extracts the comments from a specified file and writes them to a comments file.
def extract_comments(filename, filepath, comments_file):
    # Open the file in read mode
    with open(filepath, "r") as file:
        # Read the contents of the file into the 'contents' variable
        contents = file.readlines()
        # Initialize an empty list to store comments
        comments = []
        # Loop over each line in the file and check whether it starts with a '#' character
        for line in contents:
            if line.strip().startswith("#"):
                # If the line starts with a comment character, add it to the 'comments' list
                comments.append(line.strip())
        # If there are comments, write them to the comments file
        if comments:
            # Create a header with the filename and directory path
            comments_file.write(f"File: {filename}\n")
            comments_file.write(f"Directory: {os.path.dirname(filepath)}\n\n")
            # Write the comments to the file
            comments_file.write("Comments and notes:\n")
            comments_file.write("\n".join(comments))
            # Add extra newlines for readability
            comments_file.write("\n\n")

# This function extracts comments from all Python files in a specified directory and its subdirectories.
def extract_project_comments(rootdir, comments_file):
    # Loop over each item in the directory
    for file in os.listdir(rootdir):
        # Create the full file path
        filepath = os.path.join(rootdir, file)
        # If the item is a directory, call the extract_project_comments function recursively to extract comments from its files
        if os.path.isdir(filepath):
            extract_project_comments(filepath, comments_file)
        # If the item is a Python file, call the extract_comments function to extract its comments
        elif file.endswith(".py"):
            extract_comments(file, filepath, comments_file)

# Example usage
rootdir = "."  # Define the root directory as the current directory
comments_filepath = os.path.join(rootdir, "file_comments.txt")  # Define the comments file path

# Open the comments file in write mode
with open(comments_filepath, "w") as comments_file:
    # Call the extract_project_comments function to extract comments from all Python files in the root directory and its subdirectories
    extract_project_comments(rootdir, comments_file)
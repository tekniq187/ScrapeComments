# Python File Comments Extractor

This script extracts comments from Python files in a specified directory and its subdirectories and writes them to a comments file. It can be used to generate a documentation file that captures the comments and notes from the code.

## Usage

1. Place the `extract_comments.py` file in the directory where you want to extract comments from Python files.

2. Open a terminal or command prompt and navigate to the directory where the `extract_comments.py` file is located.

3. Run the script using the following command:
python extract_comments.py


4. The script will scan the directory and its subdirectories for Python files, extract the comments, and write them to a file named `file_comments.txt`.

5. After the script finishes running, you can open the `file_comments.txt` file to view the extracted comments.

## Customization

- If you want to extract comments from a specific directory other than the current directory, modify the `rootdir` variable in the code to specify the desired directory.

- By default, the extracted comments are written to a file named `file_comments.txt` in the same directory as the script. If you want to change the output file name or location, modify the `comments_filepath` variable in the code.

- The script extracts comments that start with the '#' character. If your code uses a different comment syntax, you can modify the code in the `extract_comments` function to match your comment style.

Note: This script assumes that the Python files you want to extract comments from have the '.py' file extension.


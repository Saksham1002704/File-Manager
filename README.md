**File Commander - README**

This Python script serves as a basic file command-line tool with functionalities commonly found in file explorers. Below is an explanation of its features and how to use them:

### Features:

1. **Displaying Command List (`cml`):**
   - Enter `cml` to view the available commands and their descriptions.

2. **Changing Directory (`cd`):**
   - Use `cd` to change the current working directory.
   - You will be prompted to enter the path of the directory you want to switch to.

3. **Creating a Folder (`md`):**
   - Enter `md` to create a new folder.
   - Provide the desired name for the folder when prompted.

4. **Deleting a Folder (`rd`):**
   - Enter `rd` to delete a folder.
   - You will be prompted to enter the name of the folder to delete.
   - Handles both empty and non-empty folders.

5. **Displaying Files (`ls`):**
   - Enter `ls` to display the list of files and folders in the current directory.

6. **Creating an Empty File (`copycon`):**
   - Enter `copycon` to create an empty file.
   - Specify the desired file name when prompted.

7. **Deleting a File (`del`):**
   - Enter `del` to delete a file.
   - You will be prompted to enter the name of the file to delete.

8. **Copying a File (`cp`):**
   - Enter `cp` to copy a file.
   - Provide the source file path and the destination folder path when prompted.
   - Creates the destination folder if it doesn't exist.

9. **Exiting the Loop (`ex`):**
   - Enter `ex` to exit the command loop and terminate the program.

10. **Moving or Renaming a File (`mv`):**
    - Enter `mv` to move or rename a file.
    - Provide the source file path and the destination folder path when prompted.
    - Creates the destination folder if it doesn't exist.
    - If the destination already has a file with the same name, it will be replaced.
    - Handles both file and folder movements.

### How to Run:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the command `python script_name.py` (replace `script_name.py` with the actual name of the script).

### Note:

- Ensure that you have Python installed on your system.
- Some commands may require administrator privileges.
- Exercise caution when using commands like `rd`, `del`, `cp`, and `mv`, as they can result in data loss.

Feel free to explore and customize the script according to your needs. If you encounter any issues or have suggestions for improvements, please let us know by opening an issue on GitHub. Happy file managing!

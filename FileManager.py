import os
import shutil

Command_list = ("""
cml, Command List
cd , Change directory
md , Create Folder
rd , Delete Folder
ls , Display Files
copycon , Create File
del , Delete File
ex , Exit Loop 
cp , Copy file
mv , Move or Rename fil
""")


while True:
    command = input(f"{os.getcwd()}>>")

    if command == 'md':
        file_name = input("Enter file name : ")
        os.mkdir(file_name)

    elif command == 'cd':
        try:
            path = input("Enter Path : ")
            os.chdir(path)
        except:
            print("Path Error!")

    elif command == 'rd':
        file_name = input("Enter file name : ")
        try:
            os.rmdir(file_name)
        except:
            shutil.rmtree(file_name)

    elif command == 'ls':
        l1 = os.listdir()
        for item in l1:
            print(item)

    elif command == 'copycon':
        file_name = input("Enter file name : ")
        with open(file_name , 'w') as f:
            f.write("")

    elif command == 'del':
        file_name = input("Enter file name : ")
        os.remove(file_name)

    elif command == 'cp':
        sourcefile_path = input("Enter source file path : ")
        destinationfile_path = input("Enter file destination path: ")
        shutil.os.makedirs(destinationfile_path,exist_ok=False)
        shutil.copy(sourcefile_path,destinationfile_path)

    elif command == 'ex':
        print("Exiting loop. ")
        break

    elif command == 'mv':
        sourcefile_path = input("Enter source file path : ")
        destinationfile_path = input("Enter file destination path: ")
        shutil.os.makedirs(destinationfile_path,exist_ok=True)
        shutil.move(sourcefile_path,destinationfile_path)
        try:
            shutil.rmtree(sourcefile_path)
        except:
            os.remove(sourcefile_path)
        
    elif command == 'cml':
        print(Command_list)

    else:
        print("Command Error!\nCommand not found")


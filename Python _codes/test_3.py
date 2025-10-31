import os
import glob
import pathlib


user = "Prizrak"
userLaptop = "laptop_Prizrak"

listFiles = []
nixos = pathlib.Path('/etc/nixos/')

def traverse_directories(current_path: pathlib.Path):
    for i in current_path.iterdir():
        if i.is_dir():
            print(f"Обход директории: {i}")
            listFiles.append(i)
            traverse_directories(i)
        elif i.is_file():
            print(f"Найден файл: {i}")

traverse_directories(nixos)

## FUNCTION FOR FIND MY FILES
def find_files(pattern):
    return glob.glob(pattern, recursive=True)

## MY PATHS TO FILRS
# fileWork = find_files(f'{files}/*.nix')

## FUNCTION TO MAKE A LIST NAMES OF MY FILES
def nameFile(file_paths):
    nameList = []
    for name in file_paths:
        namePath = os.path.basename(name)
        nameList.append(namePath)

    return nameList

## FUNCTION TO OPEN MY FILES BY THE PATH 
def openFile(file_paths):
    contentList = []
    for path in file_paths:
        try:
            with open(path, 'r') as f:
                content = f.read()
                contentList.append(content)
        except Exception as e:
            print(f'I dont find the file: {path}: {e}')

    return contentList
    

#for j in range(len(nameNew)):
#    for i in range(2, len(nameOld)):
#        if nameNew[j] == nameOld[i]:
#           os.system('') 
#        else:
#            print(nameNew[j], nameOld[i], False)
#            break


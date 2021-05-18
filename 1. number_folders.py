import os

def rename(old, new, path):
    old_name = os.path.join(path, old)
    new_name = os.path.join(path, new)
    os.rename(old_name, new_name)

def first_run(folders, path):
    for folder in folders:
        if not folder[0].isalpha():
            char_pos = 0
            for char in folder:
                if char.isalpha():
                    break
                char_pos += 1
            
            name = folder[char_pos:len(folder)]
            rename(folder, name, path)

def second_run(folders, path):
    amount = len(str(len(folders)))
    number = 0
    for folder in folders:
        folder_number = str(number).zfill(amount)
        name = folder_number + ' ' + folder
        number += 1
        rename(folder, name, path)

if __name__ == '__main__':
    path = input('Please provide a path: ')
    just_remove = input('Y for number the folders, N for just remove the numbers: ')
    folders = os.listdir(path)
    folders = sorted(folders)
    
    first_run(folders, path)
    if just_remove == 'Y':
        second_run(folders, path)

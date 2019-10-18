import sys
import os

BASE_DIR = os.getcwd() #must be project root directory


def get_folders(path):
    file_count=0
    folders = []    
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path, x)):
            folders.append(x)
        else:
            file_count += 1
    return folders, file_count


def show_menu(path, folders, file_count):
    print('_'*60)
    [print('>', x, end=' ') for x in path]
    print('\n')
    '''Showing only folders name '''
    for i, f in enumerate(folders):
        print('{}. {}'.format(i+1,f))
        
    if file_count > 0:
        print('\n+{} files'.format(file_count))
    print('press "B" or "b" for [BACK]')
    print('press "ENTER" to update all [index.md] of current folder')
    print('_'*60)


def update(path):
    try:
        for root, dirs, files in os.walk(os.path.join(BASE_DIR, *path)):
            curr_files = list()
            curr_folder = os.path.basename(root)
            for name in files:
                if name.endswith('.py') and not name == '__init__.py' and not dirs:
                    curr_files.append(name)

            if curr_files:
                with open(os.path.join(root, 'index.md'), mode='w') as md_file:
                    md_file.write('# Index of {}\n\n'.format(curr_folder))
                    for line in curr_files:
                        md_file.write('* [{}]({})\n'.format(line, './'+line))
                        
        print('\nUpdated index.md files')
        
    except Exception as e:
        print(e)
                        

if __name__=='__main__':
    print('Which folder to be updated?')    
    path = []
    opcode=' '
    while opcode is not '':
        if path:
            folders, file_count = get_folders(path=os.path.join(BASE_DIR, *path))
        else:
            folders = ['algorithms', 'data_structures'] #To show only two main folders
            file_count=0
            
        show_menu(path, folders, file_count)
        opcode = input('\nSelect one option: ')
        if opcode == 'B' or opcode=='b':
            if len(path)>0:
                del path[-1]
        elif opcode is '':
            update(path)    
        elif opcode.isdigit() and int(opcode) <= len(folders):
            path.append(folders[int(opcode)-1])
        else:
            print('Invalid choice')
    

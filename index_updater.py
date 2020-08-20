#!/usr/bin/env python3

import sys
import os

# Terminal parameters.
if len(sys.argv[1:]) == 0:
    print('Please, give a path')
    sys.exit(1)
else:
    mypath = sys.argv[1]

# Going through folders and subfolders.
for root, dirs, files in os.walk(mypath):
    curr_files = list()
    curr_folder = os.path.basename(root)

    for name in files:
        if name.endswith('.py') and not name == '__init__.py' and not dirs:
            curr_files.append(name)

    # If we have files, write "index.md"
    if curr_files:
        with open(os.path.join(root, 'index.md'), mode='w') as md_file:
            md_file.write('# Index of {}\n\n'.format(curr_folder))
            for line in curr_files:
                file_name = line.split('.')[0].replace('_',' ').title()
                md_file.write('* [' + file_name + '](' +line + ')\n')

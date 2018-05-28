# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:50:49 2017

@author: David Li
Helper script to create lwarpnotes, latex file should be set to \nonstopmode
Run from git bash, else the bash scripts will not work.
"""

import subprocess,os,sys

	
input_tex_file = 'reportContent.tex'
input_name, input_extension = os.path.splitext(input_tex_file)

if os.path.isfile(input_tex_file):
    print('Proceeding to produce: %s.pdf and %s_html.pdf \n' % (input_name, input_name))
else:
    print('Check the file name again \n')
	
print('Cleaning up some auxillary files')
lwarpmk_clean = ' '.join(['lwarpmk',
                    'cleanall',
                    input_name])
latexmk_clean = ' '.join(['latexmk',
                          '-C'
                        ])
try:
    subprocess.check_call(lwarpmk_clean)
    print('Calling: %s' % lwarpmk_clean)
    #subprocess.check_call(latexmk_clean)
    #print('Calling: %s' % latexmk_clean)
except subprocess.CalledProcessError:
    print('Error occured, check the command')
    pass # handle errors in the called executable
except OSError:
    print('Executable not found')
    pass # executable not found
	
# consider using command line arguments to prompt the user for input if being run from command line or hardcoded value if any arguements are passed through.
# if len(sys.argv) > 1:
    # input_tex_file = 'ELEC460Notes.tex'
# else:
    # input_tex_file = input("Enter the tex name. ")

    
cmd_str1 = ' '.join(['lualatex',
					'-synctex=1',
					'-interaction=nonstopmode',
                     input_tex_file])   
## Consider adding a loop until continueNextStage = True
#continueNextStage = False
#trials = 0
#while continueNextStage == False and trials < 3:
try:
    subprocess.check_call(cmd_str1)
    print('Calling: ' + cmd_str1)
    continueNextStage = True
except subprocess.CalledProcessError:
    print('Error occured trying to call pdflatex %s' % input_tex_file)
    #trials = trials +1 
    pass # handle errors in the called executable
except OSError:
    print('Executable not found')
    pass # executable not found

lwarpHTMLFile = input_name +'_html' + '.tex'
print('making lwarp HTML FILE: ' + lwarpHTMLFile)
cmd_str2 = ' '.join(['lualatex',
					'-synctex=1',
					'-interaction=nonstopmode',
                    lwarpHTMLFile])
try:
    subprocess.check_call(cmd_str2)
    print('Calling: %s' % cmd_str2)
except subprocess.CalledProcessError:
    print('Error occured, check the command')
    pass # handle errors in the called executable
except OSError:
    print('Executable not found')
    pass # executable not found
print('Script created final pdf without limages and glossaries.')

### Consider calling lwarpmk limages and lwarpmk htmlglossary at this point and then compiling
try:
    cmd_htmlglossary = ' '.join(['lwarpmk',
				'htmlglossary'])
    subprocess.check_call(cmd_htmlglossary)
    cmd_printglossary = ' '.join(['lwarpmk',
				'printglossary'])
    subprocess.check_call(cmd_printglossary)
    print('Creating glossary and images again for HTML.')
except subprocess.CalledProcessError:
	print('Error occured, check the command')
	pass # handle errors in the called executable
except OSError:
	print('Executable not found')
	pass # executable not found

try:
    subprocess.check_call(cmd_str1)
    print('Calling: %s' % cmd_str1)
except subprocess.CalledProcessError:
    print('Error occured, check the command')
    pass # handle errors in the called executable
except OSError:
    print('Executable not found')
    pass # executable not found
print('Script created final print pdf with glossaries.')

try:
    subprocess.check_call(cmd_str2)
    print('Calling: %s' % cmd_str2)
except subprocess.CalledProcessError:
    print('Error occured, check the command')
    pass # handle errors in the called executable
except OSError:
    print('Executable not found')
    pass # executable not found
print('Script created final pdf with limages and glossaries.')
# recompile reportContent_html.tex for glossary and images

# Produce an pdf to be converted to html
cmd_finalpdfout = ' '.join(['lualatex',
					'-synctex=1',
					'-interaction=nonstopmode',
                    lwarpHTMLFile])
					
try:
    subprocess.check_call(cmd_finalpdfout)
    print('Calling: %s' % cmd_finalpdfout)
except subprocess.CalledProcessError:
    print('Error occured, check the command')
    pass # handle errors in the called executable
except OSError:
    print('Executable not found')
    pass # executable not found
    
# Get images

import time

cmd_images = ' '.join(['lwarpmk',
				'limages'])

# lwarp 0.56 pdf to svgs or command 
# in bash shell lwarpmk pdftosvg Diagrams/*.pdf

cmd_images = ' '.join(['lwarpmk',
				'limages'])
try:
    subprocess.check_call(cmd_images)
except subprocess.CalledProcessError:
    print('Error occured when trying to process images')
    pass # handle errors in the called executable
except OSError:
    print('Executable not found for limages')
    pass # executable not found
# wait for images to load
time.sleep(7)    
    
    
print('Script is creating lwarp files, moving on to html creation.')

cmd_str3 = ' '.join(['lwarpmk',
                    'pdftohtml'])

try:
    subprocess.check_call(cmd_str3)
    print('Calling: %s' % cmd_str3)
except subprocess.CalledProcessError:
    print('Error occured, check the command')
    pass # handle errors in the called executable
except OSError:
    print('Executable not found')
    pass # executable not found
print('Script is creating lwarp files, moving on to html creation.')	
				
### Call shell script to move files
print('Moving files to correct directory')

try:
	print('./movefiles.sh')
	subprocess.call('./movefiles.sh')
except subprocess.CalledProcessError:
    print('Error occured, check the command')
    pass # handle errors in the called executable
except OSError:
    print('shell not working')
    pass # executable not found

### Call shell script to clean up files
print('Calling script to clean up files')

# try:
    # subprocess.call('sh latex-clean.sh')
# except subprocess.CalledProcessError:
    # print('Error occured, check the command')
    # pass # handle errors in the called executable
# except OSError:
    # print('shell script not working')
    # pass # executable not found
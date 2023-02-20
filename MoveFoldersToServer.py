import os
from pathlib import Path
from shutil import move
import sys
import traceback

def MoveFiles(source, destination):
    try:
        #Transform source string into path
        p = Path(source)
        #Read directory and move all folders inside it
        for f in p.iterdir():
            if f.is_dir(): #if we want to copy folders only
                # Use the os.path.join() function to construct the full paths of the source and destination directories
                src_path = os.path.join(f, '')
                dst_path = os.path.join(destination, os.path.basename(f))
                # Move the directory from src_dir to dst_dir
                move(src_path, dst_path)
    except Exception as e:
        sys.stdout.write('faild: %s\n' % e)
        traceback.print_exc()
        print('Something went wrong')
        print(e)

#Where the system will move the files from and to
#PATH 1
sourcesocialmedia = 'socialmediatemp/'
destinationsocialmedia = '/Volumes/Media/Social Media/2023/3.TO BE ORGANISED/'
#PATH 2
sourceprocessed = 'processed/'
destinationprocessed = '/Volumes/Customers/Automated-video-system-backup-multistream/'

#Base folder to start copying files
os.chdir('/Users/bigmac/Documents/GitHub/V152/VideoGenerator/data/samples/input/')

MoveFiles(sourcesocialmedia, destinationsocialmedia)
MoveFiles(sourceprocessed, destinationprocessed)


#INSTRUCTIONS TO USE AUTO SCHEDULE WITH CRONTAB (MACOS)
#Open Terminal
#Type: crontab -e
#press i to start editing and add the following
#50 7 * * * /usr/local/bin/python3 /Users/bigmac/Documents/GitHub/Moving\ Files\ to\ Server/MovingFilesPython/MoveFoldersToServer.py
#press esc
#type this to save :wq
#########
#crontab -l (Will list all scheduled jobs)
#Here is a command that creates a text file to test it
#37 10 * * * echo Miller text file > /Users/bigmac/Documents/GitHub/Moving\ Files\ to\ Server/MovingFilesPython/myfile.txt
##############
#Running Media Generator Automatically
##0 8 * * * /usr/local/bin/python3 /Users/bigmac/Documents/GitHub/AutomaticVideoEditing/main.py 

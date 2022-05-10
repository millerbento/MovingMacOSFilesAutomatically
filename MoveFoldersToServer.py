from datetime import datetime
import os
from pathlib import Path
import shutil

def MoveFiles(source, destination):
    try:
        # #Creating folder name
        # now = datetime.now()
        # folderdatename = now.strftime('%Y-%m-%d')
        # dt_string = now.strftime('%d%m%Y_%H_%M')

        # #Create a folder with today's date 
        # try:
        #         destination = destination + folderdatename
        #         os.mkdir(destination) #todaysdate
        # except:
        #         pass #folder already exist

        # #Create subfolder with the time the files were transffered
        # destination = destination + folderdatename + '/' + dt_string
        # try:
        #         os.mkdir(destination)
        # except:
        #         raise Exception('System cannot create a folder to move files')

        #Transform source string into path
        p = Path(source)
        #Read directory and move all folders inside it
        for f in p.iterdir():
                if f.is_dir(): #if we want to copy folders only
                        shutil.move(f, destination)
                
    except Exception as e:
        print('Something went wrong')
        print(e)

#Printing current directory 
directory = os.getcwd()
print(directory)

#Change the current working directory
os.chdir('/Users/maccas/Documents/New Video Maker - Miller/MoviePyMiller_V1.4/VideoGenerator/data/samples/input/')

#Printing current directory after the change
directory = os.getcwd()
print(directory)

#Where the system will move the files from and to
sourcesocialmedia = 'socialmediatemp/'
destinationsocialmedia = '/Volumes/Media/Social Media/2022/3.TO BE ORGANISED/'
sourceprocessed = 'processed/'
destinationprocessed = '/Volumes/Customers/Automated-video-system-backup/'

#Running it to move files
MoveFiles(sourcesocialmedia, destinationsocialmedia)
MoveFiles(sourceprocessed, destinationprocessed)

#AUTO SCHEDULE WITH CRONTAB
#Open Terminal
#Type: crontab -e
#press i to start editing and add the following
#0 17 * * * /usr/local/bin/python3 /Users/maccas/Documents/Moving\ Files\ to\ Server/MovingFilesPython/MoveFoldersToServer.py
#press esc
#type this to save :wq
#########
#crontab -l (Will list all scheduled jobs)
#Here is a command that creates a text file to test it
#37 10 * * * echo Miller text file > /Users/maccas/Documents/Moving\ Files\ to\ Server/MovingFilesPython/myfile.txt


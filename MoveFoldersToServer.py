print('first line')
from datetime import datetime
import os
from pathlib import Path
import shutil
from configparser import ConfigParser
print('after importing modules')

def MoveFiles(source, destination):
    try:
        #Creating folder name
        now = datetime.now()
        folderdatename = now.strftime('%Y-%m-%d')
        dt_string = now.strftime('%d%m%Y_%H_%M')

        #Create a folder with today's date 
        try:
                os.mkdir(destination + folderdatename) #todaysdate
        except:
                pass #folder already exist

        #Create subfolder with the time the files were transffered
        destination = destination + folderdatename + '/' + dt_string
        try:
                os.mkdir(destination)
        except:
                raise Exception('System cannot create a folder to move files')

        #Transform source string into path
        p = Path(source)
        #Read directory and move all folders inside it
        for f in p.iterdir():
            if f.is_dir():
                shutil.move(f, destination)
    except:
        print('Something went wrong')


#Import values from config file
file = 'config.ini'
config = ConfigParser()
config.read(file)

sourcesocialmedia = config['paths']['source1']
destinationsocialmedia = config['paths']['destination1']
sourceprocessed = config['paths']['source2']
destinationprocessed = config['paths']['destination2']

MoveFiles(sourcesocialmedia, destinationsocialmedia)
MoveFiles(sourceprocessed, destinationprocessed)
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:03:45 2021

@author: Nabila Aryanti
"""

import os

# rename files in folder terroristlogos
logospath = 'C:\\webdrivers\\imageScrapping\\dataset\\terroristlogos\\'
# Function to rename multiple files
def main():
    for count, filename in enumerate(os.listdir(logospath)):
        dst = str(count) + "_terroristlogos" + "_terrorism" + ".jpg"
        src = logospath + filename
        dst = logospath + dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)

if __name__ == '__main__':
      
    # Calling main() function
    main()
    
# rename files in folder terroristflag
flagpath = 'C:\\webdrivers\\imageScrapping\\dataset\\terroristflags\\'
# Function to rename multiple files
def main():
    for count, filename in enumerate(os.listdir(flagpath)):
        dst = str(count) + "_terroristflags" + "_terrorism" + ".jpg"
        src = flagpath + filename
        dst = flagpath + dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)

if __name__ == '__main__':
      
    # Calling main() function
    main()   
    
# rename files in folder terroristactor
actorpath = 'C:\\webdrivers\\imageScrapping\\dataset\\terroristactor\\'
# Function to rename multiple files
def main():
    for count, filename in enumerate(os.listdir(actorpath)):
        dst = str(count) + "_terroristactor" + "_terrorism" + ".jpg"
        src = actorpath + filename
        dst = actorpath + dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)
  
if __name__ == '__main__':
      
    # Calling main() function
    main() 
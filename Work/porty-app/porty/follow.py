# follow.py
#
# Exercise 6.5

import os
import time

def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
             line = f.readline()
             if line != '':
                 yield line
             else:
                 time.sleep(0.1)    # Sleep briefly to avoid busy wait
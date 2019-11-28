#! /bin/env python3

#this is for the raspberry pi to be updated via Github

#assuming the connector to the sql-server works because it is impossible to
#access on my laptop then this will be the permanent update tool used to
#atleast update relevant files on the raspberry pi

#will also need to run the parallel program in python 2.7


import os
import git
import subprocess #this one is optional for method 1 in case git library is changed
import time
import sys

def update()
    gitdir = os.getcwd() #gets current folder
    gitcmd = git.cmd.Git(gitdir)# set repository to current folder
    gitcmd.pull()# update current folder
    print("Finished pulling from GitHub")

def run_ras()
    ## here will be the funtions we will run from the other file
    #try:
    #    from raspberry_pi_stage2 import FUNCTION NAMES HERE
    #except:
    #    print("RELATED ERROR HERE")
    print("This section is still under construction")

if __name__ == '__main__':
    update()
    run_ras()
    time.sleep(36000) # for testing change from 10 hours to 5 mins(300)
    print(time.localtime())
    #line below should rerun the script
    os.exec(__file__, sys.argv)

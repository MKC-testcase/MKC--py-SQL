#the purpose of this test is to further understand the git library and how
#the files behave after an automatic pull
#this also acts as a good reminder of how python importing user created functions
#works
import os
import git
import subprocess



#initial test without functiontest
#def git_update():
    # this line identifies gitcmd as the variable to input git commands
#############THIS METHOD 1 #######################
#process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
#output = process.communicate()[0]

############# METHOD 2 ############################
gitdir = os.getcwd()

g = git.cmd.Git(gitdir)
g.pull()

print("Finished Pulling")
    #this will be the test printing a different phrase than what is listed here
    #this test will only work once if at all

#have to import after the pull
try:
    from test_gitprint import print_phrase
    print_phrase()
except:
    print("Error")


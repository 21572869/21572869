#!/usr/bin/env python
# coding: utf-8

# # Git consolidate tasks

# ## Data Science for bioinformatics

# ### Week 6 Dated on 11/11/2022

# 1. How do you determine which version of git is installed on your system and how do you install git on your operating system? 

# Ans. You can determine which version of Git is installed on your system by running the "git --version" command. To install Git on your operating system, you can download it from the official Git website (https://git-scm.com/).

# 2. How to configure your git environment?  

# Ans. 
# 1. Set your username and email:  
# git config --global user.name "Your Name"  
# git config --global user.email "your_email@example.com"  
# 
# 2. Set your default text editor:  
# git config --global core.editor nano  
# 
# 3. Set your default merge tool:  
# git config --global merge.tool kdiff3

# 3.	Create and initialize a local repository in your computer 

# Ans.
# 1. Open the terminal and navigate to the directory where you want to initialize the repository.  
# 2. Type "git init" and press enter.  
# 3. Type "git add ." and press enter.  
# 4. Type "git commit -m "Initial commit"" and press enter

# 4. Show how to sign up for a free Github account and set up a Github remote repository. 

# Ans. 
# 1. Go to github.com and create a new account.  
# 2. Follow the instructions to create a new repository.  
# 3. Once your repository is created, click on the "Settings" tab.  
# 4. In the "Collaborators" section, add your username.  
# 5. Click on the "Permissions" tab and select "Read & Write" for your username.  
# 6. Click on the "Update" button.  
# 7. Go to your local computer and navigate to the folder where your project is located.  
# 8. Type the following command: git remote add origin https://github.com/username/projectname.git  
# 9. Type the following command: git push -u origin master 

# 5.	Add the following files FileA.txt, FileB.txt into the created repository.  

# Ans. 
# $ git add FileA.txt FileB.txt  
# Stage the files for a commit.  
# $ git commit -m "Add files"  
# Commit the staged changes with a message.

# 6. Make some changes to the newly added files and demonstrate the difference in their status. 

# Ans. 
# $ git add FileA.txt FileB.txt  
# $ git commit -m "Add files FileA.txt and FileB.txt"  
# [master 2f27d70] Add files FileA.txt and FileB.txt  
# 2 files changed, 5 insertions(+)  
# create mode 100644 FileA.txt  
# create mode 100644 FileB.txt  
# 
# $ git status  
# On branch master  
# Your branch is up-to-date with 'origin/master'.  
# Untracked files:  
# (use "git add <file>..." to include in what will be committed) 	 
# FileC.txt  
# nothing added to commit but untracked files present (use "git add" to track)  
# 
# $ git add FileC.txt  
# 
# $ git commit -m "Add file FileC.txt"  
# [master 5d0e7c3] Add file FileC.txt  
# 1 file changed, 1 insertion(+)  
# create mode 100644 FileC.txt  
# 
# $ git status  
# On branch master  
# Your branch is up-to-date with 'origin/master'.  
# Changes to be committed:  
# (use "git reset HEAD <file>..." to un

# 7. Commit the files to the repository and display the history of commits in your project so far. 

# Ans. 
# git add.  
# git commit -m "add files"  
# git push origin master  
# git log 

# 8. Demonstrate how to clone a remote repository to your local workstation.  

# Ans. git clone https://github.com/USERNAME/REPOSITORY

# 9. Demonstrate how to push commits to a remote repository.  

# Ans. 
# 1) git add .  
# 2) git commit -m "Your commit message"  
# 3) git push

# 10. Demonstrate how to pull the files from a remote repository to a local repository. 

# Ans. git pull origin master

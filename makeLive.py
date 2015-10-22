#!/usr/bin/python
import subprocess
import shutil
import os

fileSite = input("Enter the file path (start from year): ") 
projectNumber = input("Enter the project number: ")
newProject = input("Is this a new project? (Type Y for yes): ")
def linkIt(filePath):
    filePath = filePath.replace("\\", "/") #take care of windows weirdness
    serverPath = "/Volumes/marketing$/Creative Services/" 
    fullFile = serverPath + filePath #add weird server path
    emailServerPath = "/Volumes/Communications/email/"
    emailServerCommon = filePath[:8] #year and main division i.e. NDS
    innerFolders = [] #list of inner divisions like i.e. MBLE_EP
    for folder in os.listdir(emailServerPath + emailServerCommon):
        if os.path.isdir(emailServerPath + emailServerCommon + "/" + folder) == True:
            innerFolders.append(folder)
    fileInnerStart = filePath.find(projectNumber)
    fileInner = filePath[9:fileInnerStart - 1] #get inner division from file path
    fileTitleStart = filePath.rfind(projectNumber)
    fileTitle = filePath[fileTitleStart:] #get file name
    def newOne():
        newDir = emailServerPath + emailServerCommon + "/" + fileInner + "/" + projectNumber
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        shutil.copy(fullFile, newDir + "/")
        print("http://www.nelnet.net/marketingprod/email/{}/{}/{}/{}".format(emailServerCommon, fileInner, projectNumber, fileTitle))
    if newProject.lower() == "y":
        newOne()
    else:
        for folder in innerFolders:
            if folder == fileInner:
                for smallFolder in os.listdir(emailServerPath + emailServerCommon + "/" + fileInner):
                    if os.path.isdir(emailServerPath + emailServerCommon + "/" + fileInner + "/" + smallFolder) == True:
                        if smallFolder == projectNumber:
                            shutil.copy(fullFile, emailServerPath + emailServerCommon + "/" + fileInner + "/" + smallFolder + "/")
                            print("http://www.nelnet.net/marketingprod/email/{}/{}/{}/{}".format(emailServerCommon, fileInner, smallFolder, fileTitle))
#things to add: fix wonky folders, make project number not input based.          

linkIt(fileSite)

'''For Grading Scale'''
import os,sys
from difflib import Differ
'''
The root folder contains folders for each chpater, this scripte would iterate all chapters, and aggregate the content of 
html and css files under each chapter to a txt file.
'''
def getHTMLandCSSFile(folder):
    folderList = os.listdir(folder);
    fileList = [];
    for f in folderList:
        if f.endswith("html"):
            fileList.append(f);
        elif f.endswith("css"):
            fileList.append(f);
        else:
            pass;
    return fileList;

folderPath = "../solution_publisher2/";
folderList = os.listdir(os.path.abspath(folderPath));
allHTMLFiles = [];
for folder in folderList:
#    print os.path.abspath(folder);
    subFolderList = getHTMLandCSSFile(os.path.abspath(folderPath)+"/"+folder);
#    print subFolderList;
    allHTMLFiles.append(subFolderList);
#print allHTMLFiles;

tempFolderPath = os.path.abspath(folderPath)+"/";
i = 0;

d = Differ();
outputFile = open("./output.txt",'w');
for tempList in allHTMLFiles:
    if i <> 0:
        for f in allHTMLFiles[i]:
            print "\n"+tempFolderPath+folderList[i]+"/"+f+"\n";
            print >>outputFile, "\n"+tempFolderPath+folderList[i]+"/"+f+"\n";
            if f in allHTMLFiles[i-1]:
                tempFile1 = open(tempFolderPath+folderList[i]+"/"+f,'r');
                file1Lines = tempFile1.readlines();
                tempFile2 = open(tempFolderPath+folderList[i-1]+"/"+f,'r');
                file2Lines = tempFile2.readlines();

                diffBetweenFiles = list(d.compare(file1Lines,file2Lines));
                for line in diffBetweenFiles:
                    if line.startswith('-'):
                        print line;
                        print >>outputFile, line+"\n";
                tempFile1.close();
                tempFile2.close();
            else:
                pass;
    print "**********************************************************************";
    print >>outputFile, "\n****************************************************************\n";

    i=i+1;
outputFile.flush();
outputFile.close();

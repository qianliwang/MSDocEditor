'''For ProgrammingHints'''
import os,sys
from docx import Document

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

folderPath = "../programmingHints/chapter14jQuery/";
htmlFileList = getHTMLandCSSFile(folderPath);

newDoc = Document();

count = 0;
for f in htmlFileList:
    newDoc.add_heading(f,level=1);
    file = open(folderPath+"/"+f,'r');
    lines = file.readlines();
    for line in lines:
        newDoc.add_paragraph(line.strip("\n\r"));

newDoc.save("test_hints.docx");

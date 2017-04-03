import os
#get file names from a folder
files = os.listdir("/Users/mac/Desktop/AI/Python/Practise/prank")

#rename the files from a folder
for file_name in files:

    os.chdir("/Users/mac/Desktop/AI/Python/Practise/prank")
    current_path = os.getcwd()
    os.rename(file_name, file_name.translate(None, "0123456789"))

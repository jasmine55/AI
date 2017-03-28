import os
#get file names from a folder
files = os.listdir("/Users/mac/Desktop/AI/Python/Practise/prank")
# print files

for file_name in files:
    # file_name = file_name.translate(None, "0123456789")
    # print file_name
    # os.rename(file_name)


    os.chdir("/Users/mac/Desktop/AI/Python/Practise/prank")
    current_path = os.getcwd()
    os.rename(file_name, file_name.translate(None, "0123456789"))

    files = os.listdir("/Users/mac/Desktop/AI/Python/Practise/prank")
    print files

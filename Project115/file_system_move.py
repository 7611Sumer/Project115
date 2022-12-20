import os

source = "/Users/navintojsinghminhas/Desktop/Project115/main.txt"
dest = "newfile.txt"

newfile = os.rename(source,dest)
print("The source file has been renamed")
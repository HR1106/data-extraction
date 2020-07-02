import re
import fileinput
for line in fileinput.input("output.txt", inplace=True):
    print(re.sub(r'Page\s\d+', "", line))
for line in fileinput.input("output.txt", inplace=True):
    print(re.sub(r'\d{2,}[.:]', "", line))
for line in fileinput.input("output.txt", inplace=True):
    print(re.sub(r'\w+\sServic.+\w+.\d+', "", line))
for line in fileinput.FileInput("output.txt",inplace=1):
    if line.rstrip():
        print(line)

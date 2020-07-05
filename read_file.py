import re
import sys


pattern = "\.js"
array = []
#file is in the same directory as the .py script
file = open("access_log.txt", "rt")
for line in file:
    if re.search(pattern, line):
        extract = line.split("/")[4]
        extract2 = extract.split(" ")[0]
        
        if len(array) < 0:
            array.append(extract2)

        if extract2 not in array:
            array.append(extract2)

        #print(extract2)

for a in array:
    print(a)

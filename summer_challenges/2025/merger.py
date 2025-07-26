import os
import re

startFile = input()

#check if path is relative
#current_dir if path is relative
startFile = os.getcwd() + "\\" + startFile

# check if file exists
file = open(startFile, "r")

reg_ex_imports = "from \\w* import \\w*"

imports = re.finditer(reg_ex_imports, file.read())

for imp in imports:
    print(imp)
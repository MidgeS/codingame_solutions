import os
import re
import traceback

importedFiles = []
reg_ex_imports = "^from\\s*[\\w*.\\w*]*\\s*import\\s*\\w*.*\\n"
reg_ex_import_file = "(?:from\\s*)([\\w*.\\w*]*)"

def cleanFileImports(file):
    print("")
    print("clean file")
    print("----------")
    resultString = ""
    fileContent = file.read()
    imports = re.finditer(reg_ex_imports, fileContent, re.MULTILINE)
    global importedFiles

    for imp in imports:
        print(imp)
        submatch = re.search(reg_ex_import_file, imp.group())
        print(submatch)
        filename = submatch.group(1)
        print("filename: "+filename)
        try:
            segments = filename.split(".")
            filepath = "\\".join(segments)
            print(filepath)
            import_file = open(os.getcwd() + "\\" + filepath+".py", "r")
            
            if filename not in importedFiles:   
                inner_result = cleanFileImports(import_file)
                print("inner")
                print(inner_result)
                importedFiles.append(filename)
                resultString = resultString + inner_result

        except Exception as e:
            print("non local import or already loaded")
            print(traceback.format_exc())

    #remove import line
    for filename in importedFiles:
        print("removing imports")
        print(filename)
        regex = f"from\\s*{filename}\\s*import\\s*\\w*.*\\n"
        print(regex)
        imp = re.search(regex, fileContent)
        print(imp)
        if imp :
            start_seg = fileContent[:imp.span()[0]]
            end_seg = fileContent[imp.span()[1]:]
            fileContent = start_seg + end_seg

    resultString = resultString + fileContent + "\r\n"
    return resultString


startFile = input()

#check if path is relative
#current_dir if path is relative
startFile = os.getcwd() + "\\" + startFile

# check if file exists
file = open(startFile, "r")

result = cleanFileImports(file)
print("RESULT FILE")
print("###########")
print("")
print(result)

output = open(os.getcwd() + "\\output.py","w+")
output.write(result)


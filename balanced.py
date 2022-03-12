#Huang,Brian
#CS-320 T/Th 14:00-15:15
#18 Feburary, 2020

import re

fileName = input("Please enter the file.")
if(len(re.findall(r'\.java',fileName)) == 0):
    print("File is not .java")
    exit()
try:
    with open(fileName) as file:
        javaFile = file.readlines()
except:
    print("The file does not exist")

def beforeQuotations(a,b): #deals with false positives from method quotations
    temp2 = re.findall(r'(\/\/|\/\*)+.*".*".*',a[b])
    if(len(temp2) > 0):
        return True
    else:
        return False

def quotations(x,y): #determines if the comments are in quotation
    if(not(beforeQuotations(x,y))):
        temp = re.findall(r'".*(\/\/|\/\*)?.*(\*\/)?.*"',x[y])
        if(len(temp) > 0):
            return True
        else:
            return False
    else:
        return False
A = True
def multiLine(c,d): #determines if /* is a multi-line
    temp3 = re.findall(r'\/\*.*\*\/',c[d])
    if(len(temp3) > 0):
        return False
    elif (len(re.findall(r'\/\*.*',c[d])) > 0):
        return True
    else:
        return False

for i in range(len(javaFile)):
    if(not(quotations(javaFile,i))):
        if(multiLine(javaFile,i)):
            while(len(re.findall(r'.*\*\/',javaFile[i])) == 0 and len(re.findall(r'.*\*\/',javaFile[i])) < len(javaFile)):
                javaFile[i] = re.sub(r'.*',"",javaFile[i])
                i = i + 1
            javaFile[i] = re.sub(r'.*\*\/',"",javaFile[i])
        else:            
            javaFile[i] = re.sub(r'\/\*.*\*\/',"",javaFile[i])
            javaFile[i] = re.sub(r'\/\/.*',"",javaFile[i])

fileName = re.sub(r'\.java',"",fileName) + ".nocom"
outfile = open(fileName,"w")
for k in range(len(javaFile)):
    outfile.write(javaFile[k])

outfile.close()

stack = []
for i in range(len(javaFile)):
    for chr in javaFile[i]:
        if(chr == "(" or chr == "{" or chr == "["):
            stack.extend(chr)
        elif(chr == ")" and stack[len(stack) - 1] == "("):
            stack.pop()
        elif(chr == "}" and stack[len(stack) - 1] == "{"):
            stack.pop()
        elif(chr == "]" and stack[len(stack) - 1] == "["):
            stack.pop()
        elif(chr == ")" or chr == "}" or chr == "]"):
            print(False)
            exit()
if(len(stack) > 0):
    print(False)
else:
    print(True)

input('Press ENTER to exit') #prevent command prompt from instantly closing to see results
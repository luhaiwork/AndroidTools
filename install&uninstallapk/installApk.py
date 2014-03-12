# encoding: utf-8
import os
mydir='C:/test/'
for path in os.listdir(mydir): 
    path=mydir+path
    print (path)
    myresult=os.popen("adb install "+path).read()
    print(myresult)

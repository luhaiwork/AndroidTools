import os
pakage='com.kstapp.fashion'
db_name='keshangtong.db'
path="/data/data/"+pakage+"/"
print("soft path :"+path)
print(os.popen("adb shell \"su -c \'cd "+path+"; chmod -R 777 databases; exit\'; exit\" ").read());
cmd = "adb pull "+path+"/databases/"+db_name ;
print(os.popen(cmd).read())


# encoding: utf-8
import os

# p = input("type pakage name ")
p="com.kstapp"
apps = os.popen("adb shell su -c ls /data/data |grep " + p).read()
yesno = input("\n pakage name:\n" + apps +"\ncomfirm to type y\n")
if yesno == 'y':
	apps = apps.split('\n')
	for app in apps :
		if len(app) != 0:
			print ("uninstall" + app)
			os.popen('adb uninstall ' + app)

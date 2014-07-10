__author__ = 'luhai'
# encoding: utf-8
import subprocess
print ("开始输入用户名称")
subprocess.call("adb shell input text test@qq.com")
subprocess.call("adb shell input keyevent 66")
print ("开始输入用户密码")
subprocess.call("adb shell input text 111111");
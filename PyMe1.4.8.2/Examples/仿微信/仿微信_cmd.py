#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
uiName="仿微信"
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 
friends = ["张三","李四","王五","赵六","群聊1"]
#初始化好友列表
def initfriends():
    for i in range(0,len(friends)):
        Fun.SetImage('好友列表',"Label_{}".format(2*i+1),".\Resources\背景.png",False)
        Fun.SetText('好友列表',"Label_{}".format(2*i+2),"")
#设置好友列表头像及名称
def setfriends(friends):
    for i in range(0,len(friends)):
        Fun.SetImage('好友列表',"Label_{}".format(2*i+1),".\Resources\{}.png".format(friends[i]),False)
        Fun.SetText('好友列表',"Label_{}".format(2*i+2),friends[i])
#搜索好友
def search(friends):
    text = Fun.GetText(uiName,"Entry_1")
    if text in friends :
        initfriends()
        setfriends([text])
    else :
        initfriends()
        Fun.MessageBox("未找到该好友")
#创建每个聊天记录文件
def creatfile():
    Result = Fun.CheckExist(".\data")
    if Result == False :
        Result = Fun.CreateDir(".\data")
    else:
        pass
    for friend in friends :
        with open('.\data\{}.txt'.format(friend),'a') as f :
            pass
#Form 'Form_1's Load Event :
def Form_1_onLoad(uiName):
    creatfile()
#LabelButton 'LabelButton_2' 's Command Event :
def LabelButton_2_onCommand(uiName,widgetName):
    Fun.LoadUIDialog(uiName,'Frame_2','好友列表')
    setfriends(friends)
#LabelButton 'LabelButton_4' 's Command Event :
def LabelButton_4_onCommand(uiName,widgetName):
    topmost = 1
    toolwindow = 1
    grab_set = 1
    wait_window = 1
    animation = ''
    params = None
    InputDataArray = Fun.CallUIDialog("通用设置",topmost,toolwindow,grab_set,wait_window,animation,params)
    print(InputDataArray)
#Entry 'Entry_1's Return Event :
def Entry_1_onReturn(event,uiName,widgetName):
    search(friends)
#Button 'Button_1' 's Command Event :
def Button_1_onCommand(uiName,widgetName):
    search(friends)
#LabelButton 'LabelButton_3' 's Command Event :
def LabelButton_3_onCommand(uiName,widgetName):
    Fun.LoadUIDialog(uiName,'Frame_2','好友列表')
    setfriends(friends)

#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
uiName="好友列表"
ElementBGArray={}
ElementBGArray_Resize={}
ElementBGArray_IM={}
friends = []
#设置好友列表头像及名称
def setfriends(friends):
    for i in range(0,len(friends)):
        Fun.SetImage(uiName,"Label_{}".format(2*i+1),".\Resources\{}.png".format(friends[i]),False)
        Fun.SetText(uiName,"Label_{}".format(2*i+2),friends[i])
        Fun.SetUserData(uiName,"Frame_{}".format(i+1),"name",friends[i])
#读取聊天记录显示在对话框
def read(name):
    value = Fun.DelAllLines(uiName,"ListBox_1")
    value = Fun.DelAllLines(uiName,"Text_2")
    with open(".\data\{}.txt".format(name),'r') as f :
        data = f.readlines()
    return data 
#Form 'Form_1's Event :Load
def Form_1_onLoad(uiName):
    pass
#Frame 'Frame_1's Button-1 Event :
def Frame_1_onButton1(event,uiName,widgetName):
    Fun.LoadUIDialog("仿微信","Frame_3","对话框")
    text = Fun.GetText(uiName,"Label_2")
    Fun.SetText("对话框","Label_1",text)
    data = read(text)
    Fun.SetValueList("对话框","ListBox_1",data)
#Frame 'Frame_2's Button-1 Event :
def Frame_2_onButton_1(event,uiName,widgetName):
    Fun.LoadUIDialog("仿微信","Frame_3","对话框")
    text = Fun.GetText(uiName,"Label_4")
    Fun.SetText("对话框","Label_1",text)
    data = read(text)
    Fun.SetValueList("对话框","ListBox_1",data)
#Frame 'Frame_3's Button-1 Event :
def Frame_3_onButton_1(event,uiName,widgetName):
    Fun.LoadUIDialog("仿微信","Frame_3","对话框")
    text = Fun.GetText(uiName,"Label_6")
    Fun.SetText("对话框","Label_1",text)
    data = read(text)
    Fun.SetValueList("对话框","ListBox_1",data)
#Frame 'Frame_4's Button-1 Event :
def Frame_4_onButton_1(event,uiName,widgetName):
    Fun.LoadUIDialog("仿微信","Frame_3","对话框")
    text = Fun.GetText(uiName,"Label_8")
    Fun.SetText("对话框","Label_1",text)
    data = read(text)
    Fun.SetValueList("对话框","ListBox_1",data)
#Frame 'Frame_5's Button-1 Event :
def Frame_5_onButton_1(event,uiName,widgetName):
    Fun.LoadUIDialog("仿微信","Frame_3","对话框")
    text = Fun.GetText(uiName,"Label_10")
    Fun.SetText("对话框","Label_1",text)
    data = read(text)
    Fun.SetValueList("对话框","ListBox_1",data)
#Label 'Label_1' 's Button-1 Event :
def Label_1_onButton_1(event,uiName,widgetName):
    Frame_1_onButton1(event,uiName,widgetName)
#Label 'Label_2' 's Button-1 Event :
def Label_2_onButton_1(event,uiName,widgetName):
    Frame_1_onButton1(event,uiName,widgetName)
#Label 'Label_3' 's Button-1 Event :
def Label_3_onButton_1(event,uiName,widgetName):
    Frame_2_onButton_1(event,uiName,widgetName)
#Label 'Label_4' 's Button-1 Event :
def Label_4_onButton_1(event,uiName,widgetName):
    Frame_2_onButton_1(event,uiName,widgetName)
#Label 'Label_5' 's Button-1 Event :
def Label_5_onButton_1(event,uiName,widgetName):
    Frame_3_onButton_1(event,uiName,widgetName)
#Label 'Label_6' 's Button-1 Event :
def Label_6_onButton_1(event,uiName,widgetName):
    Frame_3_onButton_1(event,uiName,widgetName)
#Label 'Label_7' 's Button-1 Event :
def Label_7_onButton_1(event,uiName,widgetName):
    Frame_4_onButton_1(event,uiName,widgetName)
#Label 'Label_8' 's Button-1 Event :
def Label_8_onButton_1(event,uiName,widgetName):
    Frame_4_onButton_1(event,uiName,widgetName)
#Label 'Label_9' 's Button-1 Event :
def Label_9_onButton_1(event,uiName,widgetName):
    Frame_5_onButton_1(event,uiName,widgetName)
#Label 'Label_10' 's Button-1 Event :
def Label_10_onButton_1(event,uiName,widgetName):
    Frame_5_onButton_1(event,uiName,widgetName)

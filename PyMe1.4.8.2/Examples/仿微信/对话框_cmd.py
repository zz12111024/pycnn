#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
uiName="对话框"
ElementBGArray={}
ElementBGArray_Resize={}
ElementBGArray_IM={}
#Form 'Form_1's Event :Load
#保存聊天记录
def save(name,data):
    with open(".\data\{}.txt".format(name),'a') as f :
        f.write(data)
def Form_1_onLoad(uiName):
    pass
#Button 'Button_1' 's Command Event :
def Button_1_onCommand(uiName,widgetName):
    name = Fun.GetText(uiName,"Label_1")
    data = Fun.GetText(uiName,"Text_2")
    Fun.AddItemText(uiName,"ListBox_1",data,"end")
    value = Fun.DelAllLines(uiName,"Text_2")
    save(name,data)

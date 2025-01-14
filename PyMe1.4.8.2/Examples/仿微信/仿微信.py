#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import 仿微信_cmd
import 仿微信_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  仿微信:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.configure_event = None
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=仿微信_cmd
        Fun.Register(uiName,'root',root)
        style = 仿微信_sty.SetupStyle(isTKroot)
        self.UIJsonString = '{"Version": "1.0.0", "UIName": "仿微信", "Description": "", "WindowSize": [960, 640], "WindowPosition": "Center", "WindowHide": false, "WindowResizable": true, "WindowTitle": "仿微信", "DarkMode": false, "BorderWidth": 0, "BorderColor": "#ffffff", "DropTitle": false, "DragWindow": false, "MinSize": [0, 0], "ResolutionScaling": true, "TransparentColor": null, "RootTransparency": 255, "ICOFile": null, "WinState": 1, "WinTopMost": false, "BGColor": "#EFEFEF", "GroupList": {}, "WidgetList": [{"Type": "Form", "Index": 1, "AliasName": "Form_1", "BGColor": "#EFEFEF", "Size": [960, 640], "EventList": {"Load": "Form_1_onLoad"}}, {"Type": "Frame", "Index": 2, "AliasName": "Frame_1", "ParentName": "Form_1", "PlaceInfo": [0, 0, 80, 640, "nw", true, true], "Visible": true, "Size": [80, 640], "BGColor": "#434A54", "Relief": "flat", "ScrollRegion": null}, {"Type": "LabelButton", "Index": 8, "AliasName": "LabelButton_1", "ParentName": "Frame_2", "PlaceInfo": [10, 10, 60, 60, "nw", true, true], "Visible": true, "Size": [60, 60], "Text": "", "BGColor": "#EFEFEF", "FGColor": "#000000", "BGImage": "Resources/头像.png", "Compound": "center", "BGColor_Hover": "#AAAAAA", "FGColor_Hover": "#000000", "BGColor_Click": "#AAAAAA", "FGColor_Click": "#FF0000", "Droplist": false}, {"Type": "LabelButton", "Index": 9, "AliasName": "LabelButton_2", "ParentName": "Frame_2", "PlaceInfo": [10, 80, 60, 60, "nw", true, true], "Visible": true, "Size": [60, 60], "Text": "", "BGColor": "#EFEFEF", "FGColor": "#000000", "BGImage": "Resources/ICO_PC.png", "Compound": "center", "BGColor_Hover": "#AAAAAA", "FGColor_Hover": "#000000", "BGColor_Click": "#AAAAAA", "FGColor_Click": "#FF0000", "Droplist": false, "EventList": {"Command": "LabelButton_2_onCommand"}}, {"Type": "LabelButton", "Index": 10, "AliasName": "LabelButton_3", "ParentName": "Frame_2", "PlaceInfo": [10, 150, 60, 60, "nw", true, true], "Visible": true, "Size": [60, 60], "Text": "", "BGColor": "#EFEFEF", "FGColor": "#000000", "BGImage": "Resources/ICO_Team.png", "Compound": "center", "BGColor_Hover": "#AAAAAA", "FGColor_Hover": "#000000", "BGColor_Click": "#AAAAAA", "FGColor_Click": "#FF0000", "Droplist": false, "EventList": {"Command": "LabelButton_3_onCommand"}}, {"Type": "LabelButton", "Index": 11, "AliasName": "LabelButton_4", "ParentName": "Frame_2", "PlaceInfo": [10, 220, 60, 60, "nw", true, true], "Visible": true, "Size": [60, 60], "Text": "", "BGColor": "#EFEFEF", "FGColor": "#000000", "BGImage": "Resources/ICO_Setup.png", "Compound": "center", "BGColor_Hover": "#AAAAAA", "FGColor_Hover": "#000000", "BGColor_Click": "#AAAAAA", "FGColor_Click": "#FF0000", "Droplist": false, "EventList": {"Command": "LabelButton_4_onCommand"}}, {"Type": "Frame", "Index": 6, "AliasName": "Frame_2", "ParentName": "Form_1", "PlaceInfo": [80, 80, 250, 560, "nw", true, true], "Visible": true, "Size": [250, 560], "BGColor": "#CCCCCC", "Relief": "flat", "ScrollRegion": null}, {"Type": "Frame", "Index": 7, "AliasName": "Frame_3", "ParentName": "Form_1", "PlaceInfo": [330, 0, 630, 640, "nw", true, true], "Visible": true, "Size": [630, 640], "BGColor": "#CCCCCC", "Relief": "flat", "ScrollRegion": null}, {"Type": "Entry", "Index": 4, "AliasName": "Entry_1", "ParentName": "Form_1", "PlaceInfo": [85, 20, 185, 40, "nw", true, true], "Visible": true, "Size": [185, 40], "BGColor": "#CCD1D9", "BGColor_ReadOnly": "#EFEFEF", "FGColor": "#000000", "InnerBorderColor": "#000000", "TipText": "搜索", "TipFGColor": "#888888", "Relief": "sunken", "EventList": {"Return": "Entry_1_onReturn"}}, {"Type": "Button", "Index": 12, "AliasName": "Button_1", "ParentName": "Form_1", "PlaceInfo": [280, 20, 40, 40, "nw", true, false], "Visible": true, "Size": [40, 40], "BGColor": "#CCD1D9", "Text": "", "FGColor": "#000000", "BGImage": "Resources/搜索.png", "Compound": "none", "Relief": "flat", "EventList": {"Command": "Button_1_onCommand"}}]}'
        Form_1 = Fun.CreateUIFormJson(uiName,root,isTKroot,style,self.UIJsonString)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",仿微信_cmd.Form_1_onLoad)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Configure>', self.Configure)
            
    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName,0,'')

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget and (self.configure_event is None or self.configure_event[2]!= event.width or self.configure_event[3]!= event.height):
            uiName = self.uiName
            self.configure_event = [event.x,event.y,event.width,event.height]
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            pass
#Create the root of tkinter 
if  __name__ == '__main__':
    Fun.RunApplication(仿微信)

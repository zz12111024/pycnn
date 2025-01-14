#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import 对话框_cmd
import 对话框_sty
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
class  对话框:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=对话框_cmd
        Fun.Register(uiName,'root',root)
        style = 对话框_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,960,640)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#efefef'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 960)
        Form_1.configure(height = 640)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetUIRootSize(uiName,960,640)
        #Create the elements of root 
        Text_4= EXUIControl.CustomText(Form_1,True)
        Fun.Register(uiName,'PyMe_Text_4',Text_4,'Text_2')
        Text_4.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Text_4',0,450,640,190,'nw',True,True)#lock
        Label_3 = tkinter.Label(Form_1,text="")
        Fun.Register(uiName,'PyMe_Label_3',Label_3,'Label_1')
        Fun.SetControlPlace(uiName,'PyMe_Label_3',0,0,640,80,'nw',True,True)#lock
        Label_3.configure(bg = "#EFEFEF")
        Label_3.configure(fg = "SystemButtonText")
        Label_3.configure(anchor = "w")
        Button_5 = tkinter.Button(Form_1,text="发送")
        Fun.Register(uiName,'PyMe_Button_5',Button_5,'Button_1')
        Fun.SetControlPlace(uiName,'PyMe_Button_5',520,592,120,48,'nw',True,True)
        Button_5.configure(bg = "#EFEFEF")
        Button_5.configure(command=lambda:Fun.CommandFunction_Adaptor(对话框_cmd.Button_1_onCommand,uiName,"Button_1"))
        ListBox_6 = tkinter.Listbox(Form_1)
        Fun.Register(uiName,'PyMe_ListBox_6',ListBox_6,'ListBox_1')
        Fun.SetControlPlace(uiName,'PyMe_ListBox_6',0,80,640,370,'nw',True,True)
        ListBox_6.configure(bg = "#FFFFFF")
        ListBox_6.configure(fg = "SystemButtonText")
        ListBox_6.configure(exportselection=False)
        Fun.EnableCtrlCCopyContent(uiName,'PyMe_ListBox_6')
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",对话框_cmd.Form_1_onLoad)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            
    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName)

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    Fun.RunApplication(对话框)

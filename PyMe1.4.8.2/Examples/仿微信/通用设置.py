#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import 通用设置_cmd
import 通用设置_sty
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
class  通用设置:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=通用设置_cmd
        Fun.Register(uiName,'root',root)
        style = 通用设置_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='通用设置',isDarkMode=False)
            Fun.CenterDlg(uiName,root,640,640)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#efefef'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 640)
        Form_1.configure(height = 640)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetUIRootSize(uiName,640,640)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="语言")
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'Label_1')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',104,123,100,48,'nw',True,True)
        Label_2.configure(bg = "#efefef")
        Label_2.configure(fg = "SystemButtonText")
        Label_3 = tkinter.Label(Form_1,text="通用")
        Fun.Register(uiName,'PyMe_Label_3',Label_3,'Label_2')
        Fun.SetControlPlace(uiName,'PyMe_Label_3',104,189,100,48,'nw',True,True)
        Label_3.configure(bg = "#efefef")
        Label_3.configure(fg = "SystemButtonText")
        ComboBox_4_Variable = Fun.AddTKVariable(uiName,'PyMe_ComboBox_4')
        ComboBox_4 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_4_Variable, state="normal")
        Fun.Register(uiName,'PyMe_ComboBox_4',ComboBox_4,'ComboBox_1')
        Fun.SetControlPlace(uiName,'PyMe_ComboBox_4',214,123,320,48,'nw',True,True)
        ComboBox_4["values"]=['简体中午','English','繁体中文']
        ComboBox_4.current(0)
        CheckButton_5_Variable = Fun.AddTKVariable(uiName,'PyMe_CheckButton_5')
        CheckButton_5_Variable.set(False)
        CheckButton_5 = tkinter.Checkbutton(Form_1,variable=CheckButton_5_Variable,text="有更新时自动更新",anchor=tkinter.W)
        Fun.Register(uiName,'PyMe_CheckButton_5',CheckButton_5,'CheckButton_1')
        Fun.SetControlPlace(uiName,'PyMe_CheckButton_5',214,197,319,40,'nw',True,True)
        CheckButton_5.configure(bg = "#efefef")
        CheckButton_5.configure(activebackground = "#efefef")
        CheckButton_5.configure(selectcolor = "#efefef")
        CheckButton_6_Variable = Fun.AddTKVariable(uiName,'PyMe_CheckButton_6')
        CheckButton_6_Variable.set(False)
        CheckButton_6 = tkinter.Checkbutton(Form_1,variable=CheckButton_6_Variable,text="保留聊天记录",anchor=tkinter.W)
        Fun.Register(uiName,'PyMe_CheckButton_6',CheckButton_6,'CheckButton_2')
        Fun.SetControlPlace(uiName,'PyMe_CheckButton_6',214,259,319,40,'nw',True,True)
        CheckButton_6.configure(bg = "#efefef")
        CheckButton_6.configure(activebackground = "#efefef")
        CheckButton_6.configure(selectcolor = "#efefef")
        CheckButton_7_Variable = Fun.AddTKVariable(uiName,'PyMe_CheckButton_7')
        CheckButton_7_Variable.set(False)
        CheckButton_7 = tkinter.Checkbutton(Form_1,variable=CheckButton_7_Variable,text="显示搜索记录",anchor=tkinter.W)
        Fun.Register(uiName,'PyMe_CheckButton_7',CheckButton_7,'CheckButton_3')
        Fun.SetControlPlace(uiName,'PyMe_CheckButton_7',214,320,319,40,'nw',True,True)
        CheckButton_7.configure(bg = "#efefef")
        CheckButton_7.configure(activebackground = "#efefef")
        CheckButton_7.configure(selectcolor = "#efefef")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",通用设置_cmd.Form_1_onLoad)
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
    Fun.RunApplication(通用设置)

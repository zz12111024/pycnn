#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import 好友列表_cmd
import 好友列表_sty
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
class  好友列表:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=好友列表_cmd
        Fun.Register(uiName,'root',root)
        style = 好友列表_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='好友列表',isDarkMode=False)
            Fun.CenterDlg(uiName,root,960,640)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#EFEFEF'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 960)
        Form_1.configure(height = 640)
        Form_1.configure(bg = "#EFEFEF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetUIRootSize(uiName,960,640)
        #Create the elements of root 
        Frame_20 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'PyMe_Frame_20',Frame_20,'Frame_1')
        Fun.SetControlPlace(uiName,'PyMe_Frame_20',0,0,250,70,'nw',True,True)
        Frame_20.configure(bg = "#EFEFEF")
        Frame_20.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Frame_1_onButton1,uiName=uiName,widgetName="Frame_1"))
        Label_17 = tkinter.Label(Frame_20,text="")
        Fun.Register(uiName,'PyMe_Label_17',Label_17,'Label_1')
        Fun.SetControlPlace(uiName,'PyMe_Label_17',10,10,50,50,'nw',True,True)
        Label_17.configure(bg = "#efefef")
        Label_17.configure(fg = "SystemButtonText")
        Label_17.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_1_onButton_1,uiName=uiName,widgetName="Label_1"))
        Label_18 = tkinter.Label(Frame_20,text="")
        Fun.Register(uiName,'PyMe_Label_18',Label_18,'Label_2')
        Fun.SetControlPlace(uiName,'PyMe_Label_18',60,10,180,50,'nw',True,True)
        Label_18.configure(bg = "#efefef")
        Label_18.configure(fg = "SystemButtonText")
        Label_18.configure(anchor = "w")
        Label_18.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_2_onButton_1,uiName=uiName,widgetName="Label_2"))
        Frame_21 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'PyMe_Frame_21',Frame_21,'Frame_2')
        Fun.SetControlPlace(uiName,'PyMe_Frame_21',0,70,250,70,'nw',True,True)
        Frame_21.configure(bg = "#EFEFEF")
        Frame_21.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Frame_2_onButton_1,uiName=uiName,widgetName="Frame_2"))
        Label_33 = tkinter.Label(Frame_21,text="")
        Fun.Register(uiName,'PyMe_Label_33',Label_33,'Label_3')
        Fun.SetControlPlace(uiName,'PyMe_Label_33',10,10,50,50,'nw',True,True)
        Label_33.configure(bg = "SystemButtonFace")
        Label_33.configure(fg = "SystemButtonText")
        Label_33.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_3_onButton_1,uiName=uiName,widgetName="Label_3"))
        Label_34 = tkinter.Label(Frame_21,text="")
        Fun.Register(uiName,'PyMe_Label_34',Label_34,'Label_4')
        Fun.SetControlPlace(uiName,'PyMe_Label_34',60,10,180,50,'nw',True,True)
        Label_34.configure(bg = "SystemButtonFace")
        Label_34.configure(fg = "SystemButtonText")
        Label_34.configure(anchor = "w")
        Label_34.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_4_onButton_1,uiName=uiName,widgetName="Label_4"))
        Frame_22 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'PyMe_Frame_22',Frame_22,'Frame_3')
        Fun.SetControlPlace(uiName,'PyMe_Frame_22',0,140,250,70,'nw',True,True)
        Frame_22.configure(bg = "#EFEFEF")
        Frame_22.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Frame_3_onButton_1,uiName=uiName,widgetName="Frame_3"))
        Label_35 = tkinter.Label(Frame_22,text="")
        Fun.Register(uiName,'PyMe_Label_35',Label_35,'Label_5')
        Fun.SetControlPlace(uiName,'PyMe_Label_35',10,10,50,50,'nw',True,True)
        Label_35.configure(bg = "SystemButtonFace")
        Label_35.configure(fg = "SystemButtonText")
        Label_35.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_5_onButton_1,uiName=uiName,widgetName="Label_5"))
        Label_36 = tkinter.Label(Frame_22,text="")
        Fun.Register(uiName,'PyMe_Label_36',Label_36,'Label_6')
        Fun.SetControlPlace(uiName,'PyMe_Label_36',60,10,180,50,'nw',True,True)
        Label_36.configure(bg = "SystemButtonFace")
        Label_36.configure(fg = "SystemButtonText")
        Label_36.configure(anchor = "w")
        Label_36.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_6_onButton_1,uiName=uiName,widgetName="Label_6"))
        Frame_24 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'PyMe_Frame_24',Frame_24,'Frame_4')
        Fun.SetControlPlace(uiName,'PyMe_Frame_24',0,210,250,70,'nw',True,True)
        Frame_24.configure(bg = "#EFEFEF")
        Frame_24.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Frame_4_onButton_1,uiName=uiName,widgetName="Frame_4"))
        Label_37 = tkinter.Label(Frame_24,text="")
        Fun.Register(uiName,'PyMe_Label_37',Label_37,'Label_7')
        Fun.SetControlPlace(uiName,'PyMe_Label_37',10,10,50,50,'nw',True,True)
        Label_37.configure(bg = "SystemButtonFace")
        Label_37.configure(fg = "SystemButtonText")
        Label_37.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_7_onButton_1,uiName=uiName,widgetName="Label_7"))
        Label_38 = tkinter.Label(Frame_24,text="")
        Fun.Register(uiName,'PyMe_Label_38',Label_38,'Label_8')
        Fun.SetControlPlace(uiName,'PyMe_Label_38',60,10,180,50,'nw',True,True)
        Label_38.configure(bg = "SystemButtonFace")
        Label_38.configure(fg = "SystemButtonText")
        Label_38.configure(anchor = "w")
        Label_38.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_8_onButton_1,uiName=uiName,widgetName="Label_8"))
        Frame_25 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'PyMe_Frame_25',Frame_25,'Frame_5')
        Fun.SetControlPlace(uiName,'PyMe_Frame_25',0,280,250,70,'nw',True,True)
        Frame_25.configure(bg = "#EFEFEF")
        Frame_25.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Frame_5_onButton_1,uiName=uiName,widgetName="Frame_5"))
        Label_39 = tkinter.Label(Frame_25,text="")
        Fun.Register(uiName,'PyMe_Label_39',Label_39,'Label_9')
        Fun.SetControlPlace(uiName,'PyMe_Label_39',10,10,50,50,'nw',True,True)
        Label_39.configure(bg = "SystemButtonFace")
        Label_39.configure(fg = "SystemButtonText")
        Label_39.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_9_onButton_1,uiName=uiName,widgetName="Label_9"))
        Label_40 = tkinter.Label(Frame_25,text="")
        Fun.Register(uiName,'PyMe_Label_40',Label_40,'Label_10')
        Fun.SetControlPlace(uiName,'PyMe_Label_40',60,10,180,50,'nw',True,True)
        Label_40.configure(bg = "SystemButtonFace")
        Label_40.configure(fg = "SystemButtonText")
        Label_40.configure(anchor = "w")
        Label_40.bind("<Button-1>",Fun.EventFunction_Adaptor(好友列表_cmd.Label_10_onButton_1,uiName=uiName,widgetName="Label_10"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",好友列表_cmd.Form_1_onLoad)
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
    Fun.RunApplication(好友列表)

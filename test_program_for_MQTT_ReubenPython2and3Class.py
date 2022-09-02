# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision E, 08/29/2022

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

#########################################################
from MQTT_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import argparse
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MYPRINT_FLAG

    if USE_MYPRINT_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global MQTT_ReubenPython2and3ClassObject
    global MQTT_OPEN_FLAG
    global SHOW_IN_GUI_MQTT_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            #########################################################
            #########################################################

            #########################################################
            if MQTT_OPEN_FLAG == 1 and SHOW_IN_GUI_MQTT_FLAG == 1:
                MQTT_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
            #########################################################
            #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_MQTT
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_MQTT = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MQTT, text='   MQTT   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_MQTT = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    TestButton = Button(Tab_MainControls, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_MQTT_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    argparse_Object = argparse.ArgumentParser()
    #nargs='?', const='arg_was_not_given' is the key to allowing us to not input an argument (use Pycharm "run")
    argparse_Object.add_argument("-i","--ID", nargs='?', const='arg_was_not_given', required=False, help="ID in the set [0, 1, ..., N]")
    ARGV_Dict = vars(argparse_Object.parse_args())
    print("ARGV_Dict: " + str(ARGV_Dict))

    if ARGV_Dict["ID"] != None:
        ID = int(ARGV_Dict["ID"])
    else:
        ID = 0

    print("ID: " + str(ID))
    #################################################
    #################################################

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_MQTT_FLAG
    USE_MQTT_FLAG = 1
    
    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_MQTT_FLAG
    SHOW_IN_GUI_MQTT_FLAG = 1
    
    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_MQTT
    global GUI_COLUMN_MQTT
    global GUI_PADX_MQTT
    global GUI_PADY_MQTT
    global GUI_ROWSPAN_MQTT
    global GUI_COLUMNSPAN_MQTT
    GUI_ROW_MQTT = 0

    GUI_COLUMN_MQTT = 0
    GUI_PADX_MQTT = 1
    GUI_PADY_MQTT = 1
    GUI_ROWSPAN_MQTT = 1
    GUI_COLUMNSPAN_MQTT = 1
    
    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 1

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 1
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_MQTT
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################
    global MQTT_ReubenPython2and3ClassObject

    global MQTT_OPEN_FLAG
    MQTT_OPEN_FLAG = -1

    global MQTT_ReubenPython2and3ClassObject_MostRecentDict
    MQTT_ReubenPython2and3ClassObject_MostRecentDict = dict

    global MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageCounter
    MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageCounter =  -11111.0

    global MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageTimeSeconds
    MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageTimeSeconds = -11111.0

    global MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageTopic
    MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageTopic = ""

    global MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageData
    MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageData = ""
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_MQTT = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global MQTT_GUIparametersDict
    MQTT_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MQTT_FLAG),
                                    ("root", Tab_MQTT),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_MQTT),
                                    ("GUI_COLUMN", GUI_COLUMN_MQTT),
                                    ("GUI_PADX", GUI_PADX_MQTT),
                                    ("GUI_PADY", GUI_PADY_MQTT),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_MQTT),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MQTT)])

    #################################################
    global MQTT_setup_dict

    if ID == 0:
        MQTT_setup_dict = dict([("MQTT_SERVER", "127.0.0.1"), #Input the IP address of your own MQTT server here
                                ("MQTT_Rx_topic_list", ["DebuggingRxTopic"]), #'#' means all topics
                                ("MQTT_Rx_QOS_list", [2]),
                                ("MQTT_Tx_topic_list", ["DebuggingTxTopic"]), # '#' means all topics
                                ("MQTT_Tx_QOS_list", [2]),
                                ("GUIparametersDict", MQTT_GUIparametersDict),
                                ("TxThread_TimeToSleepEachLoop", 0.002),
                                ("MQTT_RxMessage_Queue_MaxSize", 1000),
                                ("MQTT_TxMessage_Queue_MaxSize", 1000)])
    else:
        MQTT_setup_dict = dict([("MQTT_SERVER", "127.0.0.1"), #Input the IP address of your own MQTT server here
                                ("MQTT_Rx_topic_list", ["DebuggingTxTopic"]), #'#' means all topics
                                ("MQTT_Rx_QOS_list", [2]),
                                ("MQTT_Tx_topic_list", ["DebuggingRxTopic"]), # '#' means all topics
                                ("MQTT_Tx_QOS_list", [2]),
                                ("GUIparametersDict", MQTT_GUIparametersDict),
                                ("TxThread_TimeToSleepEachLoop", 0.002),
                                ("MQTT_RxMessage_Queue_MaxSize", 1000),
                                ("MQTT_TxMessage_Queue_MaxSize", 1000)])
    #################################################

    if USE_MQTT_FLAG == 1:
        try:
            MQTT_ReubenPython2and3ClassObject = MQTT_ReubenPython2and3Class(MQTT_setup_dict)
            MQTT_OPEN_FLAG = MQTT_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MQTT_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        global MyPrint_ReubenPython2and3ClassObject_GUIparametersDict
        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        global MyPrint_ReubenPython2and3ClassObject_setup_dict
        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MQTT_FLAG == 1 and MQTT_OPEN_FLAG != 1:
        print("Failed to open MQTT_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_MQTT_ReubenPython2and3ClassObject.")
    MainLoopThread_starting_time = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        MainLoopThread_current_time = getPreciseSecondsTimeStampString() - MainLoopThread_starting_time
        ###################################################

        ###################################################
        if MQTT_OPEN_FLAG == 1:

            MQTT_ReubenPython2and3ClassObject_MostRecentDict = MQTT_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "RxMessageCounter" in MQTT_ReubenPython2and3ClassObject_MostRecentDict:
                print("MQTT_ReubenPython2and3ClassObject_MostRecentDict: " + str(MQTT_ReubenPython2and3ClassObject_MostRecentDict))
                MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageCounter = MQTT_ReubenPython2and3ClassObject_MostRecentDict["RxMessageCounter"]
                MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageTimeSeconds = MQTT_ReubenPython2and3ClassObject_MostRecentDict["RxMessageTimeSeconds"]
                MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageTopic = MQTT_ReubenPython2and3ClassObject_MostRecentDict["RxMessageTopic"]
                MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageData = MQTT_ReubenPython2and3ClassObject_MostRecentDict["RxMessageData"]

                if MQTT_ReubenPython2and3ClassObject_MostRecentDict_RxMessageData.lower() == "ping":
                    MQTT_ReubenPython2and3ClassObject.AddDataToBeSent(MQTT_setup_dict["MQTT_Tx_topic_list"][0], "Received your message!", MQTT_setup_dict["MQTT_Tx_QOS_list"][0])


        else:
            time.sleep(0.005)
        ###################################################

    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_MQTT_ReubenPython2and3ClassObject.")

    #########################################################
    if MQTT_OPEN_FLAG == 1:
        MQTT_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #########################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
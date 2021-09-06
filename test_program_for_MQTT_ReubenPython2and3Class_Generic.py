# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision C, 09/05/2021

Verified working on: Python 2.7 and 3 for Windows 8.1 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

from MQTT_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *

import os, sys, platform
import time, datetime
import threading
import collections

###############
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###############

###############
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)
###############

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
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds

    global MQTT_ReubenPython2and3ClassObject
    global MQTT_OPEN_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG

    print("Exiting all threads in test_program_for_MyPrint_ReubenPython2and3Class.")

    EXIT_PROGRAM_FLAG = 1

    #########################################################
    if MQTT_OPEN_FLAG == 1:
        MQTT_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #########################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global GUI_RootAfterCallbackInterval_Milliseconds

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    TestButton = Button(root, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    #################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################
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
    GUI_PADY_MQTT = 10
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
    GUI_PADY_MYPRINT = 10
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global root

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global MQTT_ReubenPython2and3ClassObject

    global MQTT_OPEN_FLAG
    MQTT_OPEN_FLAG = -1

    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1

    global MainLoopThread_current_time
    MainLoopThread_current_time = -11111

    global MainLoopThread_starting_time
    MainLoopThread_starting_time = -11111
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
    #################################################
    #################################################

    #################################################
    #################################################
    global MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict

    global MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageCounter
    MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageCounter =  -11111.0

    global MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageTimeSeconds
    MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageTimeSeconds = -11111.0

    global MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageTopic
    MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageTopic = ""

    global MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageData
    MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageData = ""


    MQTT_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MQTT_FLAG),
                                    ("root", root),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_MQTT),
                                    ("GUI_COLUMN", GUI_COLUMN_MQTT),
                                    ("GUI_PADX", GUI_PADX_MQTT),
                                    ("GUI_PADY", GUI_PADY_MQTT),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_MQTT),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MQTT)])

    MQTT_setup_dict = dict([("MQTT_SERVER", "127.0.0.1"),
                            ("MQTT_Rx_topic_list", ["DebuggingRxTopic"]), #'#' means all topics
                            ("MQTT_Rx_QOS_list", [2]),
                            ("MQTT_Tx_topic_list", ["DebuggingTxTopic"]), # '#' means all topics
                            ("MQTT_Tx_QOS_list", [2]),
                            ("GUIparametersDict", MQTT_GUIparametersDict),
                            ("RxThread_TimeToSleepEachLoop", 0.001),
                            ("TxThread_TimeToSleepEachLoop", 0.001),
                            ("MQTT_RxMessage_Queue_MaxSize", 1000),
                            ("MQTT_TxMessage_Queue_MaxSize", 1000)])

    if USE_MQTT_FLAG == 1:
        try:
            MQTT_ReubenPython2and3ClassObject = MQTT_ReubenPython2and3Class(MQTT_setup_dict)
            time.sleep(0.25)
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

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", root),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
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
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MQTT_FLAG == 1 and MQTT_OPEN_FLAG != 1:
        print("Failed to open MQTT_ReubenPython2and3Class.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_MQTT_ReubenPython2and3ClassObject_Generic.")
    MainLoopThread_starting_time = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        MainLoopThread_current_time = getPreciseSecondsTimeStampString() - MainLoopThread_starting_time
        ###################################################

        ###################################################
        if USE_MQTT_FLAG == 1:

            MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict = MQTT_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "RxMessageCounter" in MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict:
                print("MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict: " + str(MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict))
                MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageCounter = MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict["RxMessageCounter"]
                MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageTimeSeconds = MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict["RxMessageTimeSeconds"]
                MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageTopic = MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict["RxMessageTopic"]
                MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageData = MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict["RxMessageData"]

                if MQTT_ReubenPython2and3ClassObject_MostRecentRxMessageDict_RxMessageData.lower() == "ping":
                    MQTT_ReubenPython2and3ClassObject.AddDataToBeSent(MQTT_setup_dict["MQTT_Tx_topic_list"][0], "Received your message!", MQTT_setup_dict["MQTT_Tx_QOS_list"][0])


        else:
            time.sleep(0.005)
        ###################################################

    #################################################
    #################################################

    print("Exiting main program 'test_program_for_MQTT_ReubenPython2and3ClassObject_Generic.")
    ##########################################################################################################
    ##########################################################################################################
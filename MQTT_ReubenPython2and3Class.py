# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision G, 05/10/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

#########################################################
import os, sys, platform
import time, datetime
import inspect #To enable 'TellWhichFileWereIn'
import threading
import select
import re
import collections
from copy import * #for deepcopy
import random
from random import randint
import atexit #This line keeps the console window open so that we can see error messages from a program crash before the console window is closed.
import traceback
#########################################################

#########################################################
import paho.mqtt.client as mqtt #"sudo pip install paho-mqtt" works on windows (without sudo) and Raspberry Pi
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

#########################################################
if sys.version_info[0] < 3:
    import Queue  # Python 2
else:
    import queue as Queue  # Python 3
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input
######################################################### "sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)

class MQTT_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame
    ##########################################################################################################
    ##########################################################################################################
    def __init__(self, setup_dict):

        print("#################### MQTT_ReubenPython2and3Class __init__ starting. ####################")

        self.EXIT_PROGRAM_FLAG = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 0
        self.EnableInternal_MyPrint_Flag = 0

        #########################################################
        #########################################################
        if platform.system() == "Linux":

            if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
                self.my_platform = "pi"
            else:
                self.my_platform = "linux"

        elif platform.system() == "Windows":
            self.my_platform = "windows"

        elif platform.system() == "Darwin":
            self.my_platform = "mac"

        else:
            self.my_platform = "other"

        print("The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            #########################################################
            #########################################################
            if "USE_GUI_FLAG" in self.GUIparametersDict:
                self.USE_GUI_FLAG = self.PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG", self.GUIparametersDict["USE_GUI_FLAG"])
            else:
                self.USE_GUI_FLAG = 0

            print("MQTT_ReubenPython2and3Class __init__: USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("MQTT_ReubenPython2and3Class __init__: Error, must pass in 'root'")
                return
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = self.PassThrough0and1values_ExitProgramOtherwise("EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("MQTT_ReubenPython2and3Class __init__: EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = self.PassThrough0and1values_ExitProgramOtherwise("PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("MQTT_ReubenPython2and3Class __init__: PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("MQTT_ReubenPython2and3Class __init__: NumberOfPrintLines: " + str(self.NumberOfPrintLines))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("MQTT_ReubenPython2and3Class __init__: UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("MQTT_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("MQTT_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("MQTT_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("MQTT_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 1.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("MQTT_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 1.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("MQTT_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            #########################################################
            #########################################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("MQTT_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        #print("MQTT_ReubenPython2and3Class __init__: GUIparametersDict = " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_SERVER" in setup_dict:
            self.MQTT_SERVER = setup_dict["MQTT_SERVER"]
        else:
            self.MQTT_SERVER = "default"

        print("MQTT_ReubenPython2and3Class __init__: MQTT_SERVER: " + str(self.MQTT_SERVER))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_USERNAME" in setup_dict:
            self.MQTT_USERNAME = setup_dict["MQTT_USERNAME"]
        else:
            self.MQTT_USERNAME = "default"

        print("MQTT_ReubenPython2and3Class __init__: MQTT_USERNAME: " + str(self.MQTT_USERNAME))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_PASSWORD" in setup_dict:
            self.MQTT_PASSWORD = setup_dict["MQTT_PASSWORD"]
        else:
            self.MQTT_PASSWORD = "default"

        print("MQTT_ReubenPython2and3Class __init__: MQTT_PASSWORD: " + str(self.MQTT_PASSWORD))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_PORT" in setup_dict:
            self.MQTT_PORT = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MQTT_PORT", setup_dict["MQTT_PORT"], 0.0, 1000000.0))
        else:
            self.MQTT_PORT = 1883

        print("MQTT_ReubenPython2and3Class __init__: MQTT_PORT: " + str(self.MQTT_PORT))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_KEEPALIVE" in setup_dict:
            self.MQTT_KEEPALIVE = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MQTT_KEEPALIVE", setup_dict["MQTT_KEEPALIVE"], 0.0, 1000.0))
        else:
            self.MQTT_KEEPALIVE = 60

        print("MQTT_ReubenPython2and3Class __init__: MQTT_KEEPALIVE: " + str(self.MQTT_KEEPALIVE))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_Rx_topic_list" in setup_dict:
            self.MQTT_Rx_topic_list = setup_dict["MQTT_Rx_topic_list"]

            ##############
            if self.IsInputList(self.MQTT_Rx_topic_list) == 0:
                self.MQTT_Rx_topic_list = list([self.MQTT_Rx_topic_list])
            ##############
            
            ##############
            RedundancyCheckList = list()
            for element in self.MQTT_Rx_topic_list:
                if element in RedundancyCheckList:
                    print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Rx_topic_list' must not contain duplicate values.")
                    return
                else:
                    if type(element) != str:
                        print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Rx_topic_list' must contain all strings.")
                        return
                    else:
                        RedundancyCheckList.append(element)
            ##############
                        
        else:
            self.MQTT_Rx_topic_list = ["#"] #Listens to all channels
            
        print("MQTT_ReubenPython2and3Class __init__: MQTT_Rx_topic_list: " + str(self.MQTT_Rx_topic_list))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_Rx_QOS_list" in setup_dict:
            self.MQTT_Rx_QOS_list = setup_dict["MQTT_Rx_QOS_list"]

            ##############
            if self.IsInputList(self.MQTT_Rx_QOS_list) == 0:
                self.MQTT_Rx_QOS_list = list([self.MQTT_Rx_QOS_list])
            ##############

            ##############
            for element in self.MQTT_Rx_QOS_list:
                if element not in [1, 2, 3]:
                    print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Rx_QOS' must have a value or 1, 2, or 3.")
                    return
            ##############

        else:
            self.MQTT_Rx_QOS_list = [2]*len(self.MQTT_Rx_topic_list) #Default to best quality

        print("MQTT_ReubenPython2and3Class __init__: MQTT_Rx_QOS_list: " + str(self.MQTT_Rx_QOS_list))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if len(self.MQTT_Rx_topic_list) != len(self.MQTT_Rx_QOS_list):
            print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Rx_topic_list' must be the same length as 'MQTT_Rx_QOS_list'.")
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_Tx_topic_list" in setup_dict:
            self.MQTT_Tx_topic_list = setup_dict["MQTT_Tx_topic_list"]

            ##############
            if self.IsInputList(self.MQTT_Tx_topic_list) == 0:
                self.MQTT_Tx_topic_list = list([self.MQTT_Tx_topic_list])
            ##############

            ##############
            RedundancyCheckList = list()
            for element in self.MQTT_Tx_topic_list:
                if element in RedundancyCheckList:
                    print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Tx_topic_list' must not contain duplicate values.")
                    return
                else:
                    if type(element) != str:
                        print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Tx_topic_list' must contain all strings.")
                        return
                    else:
                        RedundancyCheckList.append(element)
            ##############

        else:
            self.MQTT_Tx_topic_list = ["#"]  # Listens to all channels

        print("MQTT_ReubenPython2and3Class __init__: MQTT_Tx_topic_list: " + str(self.MQTT_Tx_topic_list))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_Tx_QOS_list" in setup_dict:
            self.MQTT_Tx_QOS_list = setup_dict["MQTT_Tx_QOS_list"]

            ##############
            if self.IsInputList(self.MQTT_Tx_QOS_list) == 0:
                self.MQTT_Tx_QOS_list = list([self.MQTT_Tx_QOS_list])
            ##############

            ##############
            for element in self.MQTT_Tx_QOS_list:
                if element not in [1, 2, 3]:
                    print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Tx_QOS' must have a value or 1, 2, or 3.")
                    return
            ##############

        else:
            self.MQTT_Tx_QOS_list = [2]*len(self.MQTT_Tx_topic_list) #Default to best quality

        print("MQTT_ReubenPython2and3Class __init__: MQTT_Tx_QOS_list: " + str(self.MQTT_Tx_QOS_list))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if len(self.MQTT_Tx_topic_list) != len(self.MQTT_Tx_QOS_list):
            print("MQTT_ReubenPython2and3Class __init__: Error, 'MQTT_Tx_topic_list' must be the same length as 'MQTT_Tx_QOS_list'.")
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "TxThread_TimeToSleepEachLoop" in setup_dict:
            if self.my_platform == "pi": #Must have at least 0.001 sleep in each loop, or the RaspPi will seize-up!
                self.TxThread_TimeToSleepEachLoop = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("TxThread_TimeToSleepEachLoop", setup_dict["TxThread_TimeToSleepEachLoop"], 0.001, 100000)
            else:
                self.TxThread_TimeToSleepEachLoop = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("TxThread_TimeToSleepEachLoop", setup_dict["TxThread_TimeToSleepEachLoop"], 0.000, 100000)

        else:
            self.TxThread_TimeToSleepEachLoop = 0.002

        print("MQTT_ReubenPython2and3Class __init__: TxThread_TimeToSleepEachLoop: " + str(self.TxThread_TimeToSleepEachLoop))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_RxMessage_Queue_MaxSize" in setup_dict:
            self.MQTT_RxMessage_Queue_MaxSize = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MQTT_RxMessage_Queue_MaxSize", setup_dict["MQTT_RxMessage_Queue_MaxSize"], 0.000, 100000))

        else:
            self.MQTT_RxMessage_Queue_MaxSize = 100

        print("MQTT_ReubenPython2and3Class __init__: MQTT_RxMessage_Queue_MaxSize: " + str(self.MQTT_RxMessage_Queue_MaxSize))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MQTT_TxMessage_Queue_MaxSize" in setup_dict:
            self.MQTT_TxMessage_Queue_MaxSize = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MQTT_TxMessage_Queue_MaxSize", setup_dict["MQTT_TxMessage_Queue_MaxSize"], 0.000, 100000))

        else:
            self.MQTT_TxMessage_Queue_MaxSize = 100

        print("MQTT_ReubenPython2and3Class __init__: MQTT_TxMessage_Queue_MaxSize: " + str(self.MQTT_TxMessage_Queue_MaxSize))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.PrintToGui_Label_TextInputHistory_List = [" "]*self.NumberOfPrintLines
        self.PrintToGui_Label_TextInput_Str = ""
        self.GUI_ready_to_be_updated_flag = 0
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        random.seed()
        self.MQTT_CLIENT_ID = str(randint(10000,999999999))  #Assign a randomly-generated integer so that we never have duplicate IDs, which would crash one of the programs
        self.MQTT_connected_flag = False
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.LoopCounter_CalculatedFromRxThread = 0
        self.CurrentTime_CalculatedFromRxThread = -11111.0
        self.LastTime_CalculatedFromRxThread = -11111.0
        self.DataStreamingFrequency_CalculatedFromRxThread = -1
        self.DataStreamingDeltaT_CalculatedFromRxThread = -1
        self.Starting_CalculatedFromRxThread = self.getPreciseSecondsTimeStampString()
        self.RxThread_still_running_flag = 1

        self.MQTT_RxMessage_Queue = Queue.Queue()

        self.MostRecentRxMessageDict = dict([("RxMessageCounter", -11111),
                                             ("RxMessageTimeSeconds", -11111.0),
                                             ("RxMessageFrequencyHz", -11111.0),
                                             ("RxMessageData", ""),
                                             ("RxMessageTopic", "")])
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.LoopCounter_CalculatedFromTxThread = 0
        self.CurrentTime_CalculatedFromTxThread = -11111.0
        self.LastTime_CalculatedFromTxThread = -11111.0
        self.DataStreamingFrequency_CalculatedFromTxThread = -1
        self.DataStreamingDeltaT_CalculatedFromTxThread = -1
        self.Starting_CalculatedFromTxThread = self.getPreciseSecondsTimeStampString()
        self.TxThread_still_running_flag = 1

        self.MQTT_TxMessage_Queue = Queue.Queue()

        self.MostRecentTxMessageDict = dict([("TxMessageCounter", -11111),
                                             ("TxMessageTimeSeconds", -11111.0),
                                             ("TxMessageFrequencyHz", -11111.0),
                                             ("TxMessageData", ""),
                                             ("TxMessageTopic", "")])
        #########################################################
        #########################################################

        print("#################### MQTT_ReubenPython2and3Class __init__ ended input-parameter parsing and variable initialization. ####################")

        #########################################################
        #########################################################
        self.MQTT_OpenCommunication()
        #########################################################
        #########################################################

        ######################################################### unicorn
        #########################################################
        #self.RxThread_ThreadingObject = threading.Thread(target=self.RxThread, args=())
        #self.RxThread_ThreadingObject.start()

        #WE'LL BE USING MQTT_OnMessage_Callback instead of the normal RxThread!
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.TxThread_ThreadingObject = threading.Thread(target=self.TxThread, args=())
        self.TxThread_ThreadingObject.start()
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if self.USE_GUI_FLAG == 1:
            self.StartGUI(self.root)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        time.sleep(0.25)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
        #########################################################
        #########################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def __del__(self):
        pass
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber):

        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be 0 or 1 (value was " +
                          str(InputNumber_ConvertedToFloat) +
                          "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue):
        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat >= RangeMinValue and InputNumber_ConvertedToFloat <= RangeMaxValue:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be in the range [" +
                          str(RangeMinValue) +
                          ", " +
                          str(RangeMaxValue) +
                          "] (value was " +
                          str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def getTimeStampString(self):

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('date-%m-%d-%Y---time-%H-%M-%S')

        return st
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def getPreciseSecondsTimeStampString(self):
        ts = time.time()

        return ts
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def TellWhichFileWereIn(self):

        #We used to use this method, but it gave us the root calling file, not the class calling file
        #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

        frame = inspect.stack()[1]
        filename = frame[1][frame[1].rfind("\\") + 1:]
        filename = filename.replace(".py","")

        return filename
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetMostRecentDataDict(self):

        if self.EXIT_PROGRAM_FLAG == 0:

            if self.MQTT_RxMessage_Queue.qsize() > 0:
                RxMessageToReturn_LocalCopy = self.MQTT_RxMessage_Queue.get()

                #deepcopy is NOT required as RxMessageToReturn_LocalCopy only contains numbers and strings (no lists, dicts, etc. that go beyond 1-level).
                return RxMessageToReturn_LocalCopy.copy()

            else:
                return dict()

        else:
            return dict() #So that we're not returning variables during the close-down process.
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def MQTT_OnConnect_Callback(self, client, userdata, flags, rc):

        if(rc == 0):

            self.MyPrint_WithoutLogFile("MQTT_OnConnect_Callback event fire: MQTT connected!")
            self.MQTT_connected_flag = True

            for Rx_list_index in range(0, len(self.MQTT_Rx_topic_list)):
                self.MQTTclientObject.subscribe(self.MQTT_Rx_topic_list[Rx_list_index], qos = self.MQTT_Rx_QOS_list[Rx_list_index])
                self.MyPrint_WithoutLogFile("Subscribed to Rx topic " + self.MQTT_Rx_topic_list[Rx_list_index] + " with QOS = " + str(self.MQTT_Rx_QOS_list[Rx_list_index]))

            for Tx_list_index in range(0, len(self.MQTT_Tx_topic_list)):
                self.MQTTclientObject.subscribe(self.MQTT_Tx_topic_list[Tx_list_index], qos = self.MQTT_Tx_QOS_list[Tx_list_index])
                self.MyPrint_WithoutLogFile("Subscribed to Tx topic " + self.MQTT_Tx_topic_list[Tx_list_index] + " with QOS = " + str(self.MQTT_Tx_QOS_list[Tx_list_index]))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ########################################################################################################## unicorn
    def MQTT_OnMessage_Callback(self, client, userdata, ReceivedMessageRaw, AllowBytesLiteralsFlag = 0):

        MQTT_RxMessage_Topic_LocalCopy = str(ReceivedMessageRaw.topic)

        if MQTT_RxMessage_Topic_LocalCopy not in self.MQTT_Rx_topic_list: #We don't want to be listening to random messages
            return

        ####################
        if AllowBytesLiteralsFlag == 0:
            MQTT_RxMessage_Data_Str_LocalCopy = str(ReceivedMessageRaw.payload.decode())
        else:
            MQTT_RxMessage_Data_Str_LocalCopy = str(ReceivedMessageRaw.payload)
        ####################

        #self.MyPrint_WithoutLogFile("MQTT_OnMessage_Callback, Topic: " + MQTT_RxMessage_Topic_LocalCopy + " , Payload: " + MQTT_RxMessage_Data_Str_LocalCopy)

        if str(ReceivedMessageRaw.payload) != self.MostRecentTxMessageDict["TxMessageData"] and str(ReceivedMessageRaw.payload.decode()) != self.MostRecentTxMessageDict["TxMessageData"]: #Check that we're not reading the message we just sent

            self.CurrentTime_CalculatedFromRxThread = self.getPreciseSecondsTimeStampString() - self.Starting_CalculatedFromRxThread
            self.UpdateFrequencyCalculation_CalculatedFromRxThread()

            tempDict = dict([("RxMessageCounter", self.LoopCounter_CalculatedFromRxThread),
                             ("RxMessageTimeSeconds", self.CurrentTime_CalculatedFromRxThread),
                             ("RxMessageFrequencyHz", self.DataStreamingFrequency_CalculatedFromRxThread),
                             ("RxMessageData", MQTT_RxMessage_Data_Str_LocalCopy),
                             ("RxMessageTopic", MQTT_RxMessage_Topic_LocalCopy)])

            self.MostRecentRxMessageDict = tempDict

            if self.MQTT_RxMessage_Queue.qsize() < self.MQTT_RxMessage_Queue_MaxSize:
                self.MQTT_RxMessage_Queue.put(tempDict)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def __MQTT_send_data(self, MQTT_TxMessageToSend_Topic, MQTT_TxMessageToSend_Data_Str, MQTT_TxMessageToSend_QOS):

        if self.MQTT_connected_flag == True:
            MQTT_TxMessageToSend_Data_Str = str(MQTT_TxMessageToSend_Data_Str)
            self.MQTTclientObject.publish(MQTT_TxMessageToSend_Topic, MQTT_TxMessageToSend_Data_Str, qos = MQTT_TxMessageToSend_QOS, retain=False)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def AddDataToBeSent(self, MQTT_TxMessageToSend_Topic, MQTT_TxMessageToSend_Data_Str, MQTT_TxMessageToSend_QOS):
        
        if self.MQTT_TxMessage_Queue.qsize() < self.MQTT_TxMessage_Queue_MaxSize:
            MQTT_TxMessageToSend_Data_Str = str(MQTT_TxMessageToSend_Data_Str)
            self.MQTT_TxMessage_Queue.put(dict([("TxMessageTopic", MQTT_TxMessageToSend_Topic),("TxMessageData", MQTT_TxMessageToSend_Data_Str),("TxMessageQOS", MQTT_TxMessageToSend_QOS)]))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def MQTT_OnPublish_Callback(self, client, userdata, mid):
        pass

        #self.MyPrint_WithoutLogFile("MQTT_OnPublish_Callback: Published!")
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def MQTT_OnDisconnect_Callback(self, client, userdata, rc):

        if self.MQTT_connected_flag == False:
            self.MyPrint_WithoutLogFile("MQTT_on_disconnect: MQTT client disconnected, reconnecting.")
            self.MQTTclientObject.connect(self.MQTT_SERVER, self.MQTT_PORT)
            while(self.MQTT_connected_flag == False):
                self.MQTTclientObject.loop(timeout=0.1)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def MQTT_OpenCommunication(self):

        try:
            self.MyPrint_WithoutLogFile("Attempting to connect to MQTT broker")

            self.MQTTclientObject = mqtt.Client(client_id = self.MQTT_CLIENT_ID, clean_session=True)
            
            self.MQTTclientObject.user_data_set(self.MQTT_CLIENT_ID)
            self.MQTTclientObject.on_publish = self.MQTT_OnPublish_Callback
            self.MQTTclientObject.on_connect = self.MQTT_OnConnect_Callback
            self.MQTTclientObject.on_disconnect = self.MQTT_OnDisconnect_Callback
            self.MQTTclientObject.on_message = self.MQTT_OnMessage_Callback

            if self.MQTT_USERNAME != "default" and self.MQTT_PASSWORD != "default":
                self.MQTTclientObject.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)

            self.MQTTclientObject.connect(self.MQTT_SERVER, int(self.MQTT_PORT), int(self.MQTT_KEEPALIVE))

            while (self.MQTT_connected_flag == False):
                self.MQTTclientObject.loop(timeout=0.1)

            self.MQTTclientObject.loop_start() #Now MQTT will perform client.loop(timeout=0.01) in its own thread so that I don't have to call it explicitly anymore
            #time.sleep(0.5)

            self.MyPrint_WithoutLogFile("MQTT Communication Connected!")
            return 1
        
        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("MQTT_OpenCommunication ERROR: Exceptions: %s" % exceptions)
            traceback.print_exc()
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_CalculatedFromRxThread(self):

        try:

            self.DataStreamingDeltaT_CalculatedFromRxThread = self.CurrentTime_CalculatedFromRxThread - self.LastTime_CalculatedFromRxThread

            ##########################
            if self.DataStreamingDeltaT_CalculatedFromRxThread != 0.0:
                self.DataStreamingFrequency_CalculatedFromRxThread = 1.0/self.DataStreamingDeltaT_CalculatedFromRxThread
            ##########################

            self.LastTime_CalculatedFromRxThread = self.CurrentTime_CalculatedFromRxThread

            self.LoopCounter_CalculatedFromRxThread = self.LoopCounter_CalculatedFromRxThread + 1

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_CalculatedFromRxThread ERROR, exceptions: %s" % exceptions)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_CalculatedFromTxThread(self):

        try:

            self.DataStreamingDeltaT_CalculatedFromTxThread = self.CurrentTime_CalculatedFromTxThread - self.LastTime_CalculatedFromTxThread

            ##########################
            if self.DataStreamingDeltaT_CalculatedFromTxThread != 0.0:
                self.DataStreamingFrequency_CalculatedFromTxThread = 1.0/self.DataStreamingDeltaT_CalculatedFromTxThread
            ##########################

            self.LastTime_CalculatedFromTxThread = self.CurrentTime_CalculatedFromTxThread

            self.LoopCounter_CalculatedFromTxThread = self.LoopCounter_CalculatedFromTxThread + 1

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_CalculatedFromTxThread ERROR, exceptions: %s" % exceptions)
    ##########################################################################################################
    ##########################################################################################################

    #######################################################################################################################
    #######################################################################################################################
    #######################################################################################################################
    #######################################################################################################################
    ####################################################################################################################### unicorn
    def TxThread(self):

        print("Started the TxThread thread for MQTT_ReubenPython2and3Class object.")
        self.TxThread_still_running_flag = 1

        #############################################################################################################################################
        #############################################################################################################################################
        #############################################################################################################################################
        #############################################################################################################################################
        while self.EXIT_PROGRAM_FLAG == 0:

            try:
                ##################################################################################################################
                ##################################################################################################################
                ##################################################################################################################

                ################################################################################################################
                ################################################################################################################
                if self.MQTT_TxMessage_Queue.qsize() > 0:
                    TxMessageToSend_LocalCopy_Dict = self.MQTT_TxMessage_Queue.get()

                    self.CurrentTime_CalculatedFromTxThread = self.getPreciseSecondsTimeStampString() - self.Starting_CalculatedFromTxThread
                    self.UpdateFrequencyCalculation_CalculatedFromTxThread()  # ONLY UPDATE IF WE HAD NEW DATA

                    tempDict = dict([("TxMessageCounter", self.LoopCounter_CalculatedFromTxThread),
                                     ("TxMessageTimeSeconds", self.CurrentTime_CalculatedFromTxThread),
                                     ("TxMessageFrequencyHz", self.DataStreamingFrequency_CalculatedFromTxThread),
                                     ("TxMessageData", TxMessageToSend_LocalCopy_Dict["TxMessageData"]),
                                     ("TxMessageTopic", TxMessageToSend_LocalCopy_Dict["TxMessageTopic"])])

                    self.MostRecentTxMessageDict = tempDict

                    self.__MQTT_send_data(TxMessageToSend_LocalCopy_Dict["TxMessageTopic"], TxMessageToSend_LocalCopy_Dict["TxMessageData"], TxMessageToSend_LocalCopy_Dict["TxMessageQOS"]) #This function can ONLY be called internally
                ################################################################################################################
                ################################################################################################################

                ################################################################################################################
                ################################################################################################################
                if self.TxThread_TimeToSleepEachLoop > 0.0:
                    time.sleep(self.TxThread_TimeToSleepEachLoop)
                ################################################################################################################
                ################################################################################################################

                ##################################################################################################################
                ##################################################################################################################
                ##################################################################################################################

            except:
                exceptions = sys.exc_info()[0]
                print("MQTT_ReubenPython2and3Class TxThread: Exceptions: %s" % exceptions)

        #############################################################################################################################################
        #############################################################################################################################################
        #############################################################################################################################################
        #############################################################################################################################################

        print("Finished the TxThread for MQTT_ReubenPython2and3Class object.")
        self.TxThread_still_running_flag = 0

    #######################################################################################################################
    #######################################################################################################################
    #######################################################################################################################
    #######################################################################################################################
    #######################################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):

        print("Exiting all threads for MQTT_ReubenPython2and3Class object")

        self.EXIT_PROGRAM_FLAG = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StartGUI(self, GuiParent):

        #self.GUI_Thread_ThreadingObject = threading.Thread(target=self.GUI_Thread, args=(GuiParent,))
        #self.GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        #self.GUI_Thread_ThreadingObject.start()

        self.GUI_Thread(GuiParent)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_Thread(self, parent):

        print("Starting the GUI_Thread for MyPrintClassPython3exp2 object.")

        #########################################################
        #########################################################
        self.root = parent
        self.parent = parent
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.myFrame = Frame(self.root)

        if self.UseBorderAroundThisGuiObjectFlag == 1:
            self.myFrame["borderwidth"] = 2
            self.myFrame["relief"] = "ridge"

        self.myFrame.grid(row = self.GUI_ROW,
                          column = self.GUI_COLUMN,
                          padx = self.GUI_PADX,
                          pady = self.GUI_PADY,
                          rowspan = self.GUI_ROWSPAN,
                          columnspan= self.GUI_COLUMNSPAN)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.MQTT_Rx_Label = Label(self.myFrame, text="MQTT_Rx_Label", width=50)
        self.MQTT_Rx_Label.grid(row=1, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.MQTT_Tx_Label = Label(self.myFrame, text="MQTT_Tx_Label", width=50)
        self.MQTT_Tx_Label.grid(row=2, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.PullDownMenu_TxTopics_StrVar = StringVar(self.myFrame)

        if sys.version_info[0] < 3: #Python 2

            #########################################################
            listvariable_str = ' '.join([str(elem) for elem in self.MQTT_Tx_topic_list]) #Convert a list of strings into a single string which contains each list element with a space in between
            self.PullDownMenu_TxTopics_StrVar.set(listvariable_str)

            ListBoxNumberOfLinesToShow = len(self.MQTT_Tx_topic_list)
            self.PullDownMenu_TxTopics = Listbox(self.myFrame, height=ListBoxNumberOfLinesToShow, width=50, listvariable=self.PullDownMenu_TxTopics_StrVar, selectmode=SINGLE)


            #self.PullDownMenu_TxTopics = Listbox(self.myFrame, height=ListBoxNumberOfLinesToShow, width=50, selectmode=SINGLE)
            #THIS METHOD 'insert' IS AN ALTERNATIVE TO THE 'listvariable'
            #for counter, element in enumerate(self.MQTT_Tx_topic_list):
            #    self.PullDownMenu_TxTopics.insert(counter, element)

            #self.PullDownMenu_TxTopics.bind('<<ListboxSelect>>', lambda event, name="ListboxSelect": self.PullDownMenu_TxTopics_CallbackFunction(event, name))

            #self.PullDownMenu_TxTopics.selection_anchor(0) #DOES NOT WORK IN PYTHON 2
            #self.PullDownMenu_TxTopics.select_set(0, 0)   #DOES NOT WORK IN PYTHON 2
            #self.PullDownMenu_TxTopics.selection_set(0) #DOES NOT WORK IN PYTHON 2
            #self.PullDownMenu_TxTopics.see(0) #DOES NOT WORK IN PYTHON 2
            #self.PullDownMenu_TxTopics.activate(0) #DOES NOT WORK IN PYTHON 2
            #########################################################

        else: #Python 3
            #########################################################
            #'''
            self.PullDownMenu_TxTopics_StrVar.set(self.MQTT_Tx_topic_list[0]) #Default value
            self.PullDownMenu_TxTopics = OptionMenu(self.myFrame, self.PullDownMenu_TxTopics_StrVar, *self.MQTT_Tx_topic_list) #, justify=CENTER, anchor=CENTER
            #'''
            #########################################################

            #########################################################
            '''
            self.PullDownMenu_TxTopics_StrVar.set(self.MQTT_Tx_topic_list[0])  # Default value
            self.PullDownMenu_TxTopics = ttk.Combobox(self.myFrame, textvariable = self.PullDownMenu_TxTopics_StrVar, values = self.MQTT_Tx_topic_list)
            '''
            #########################################################

            #########################################################
            '''
            self.PullDownMenu_TxTopics_StrVar.set(self.MQTT_Tx_topic_list[0])  # Default value
            self.PullDownMenu_TxTopics_MenuButton = Menubutton(self.myFrame, text="Select Tx Topic")
            self.PullDownMenu_TxTopics_MenuButton.menu = Menu(self.PullDownMenu_TxTopics_MenuButton, tearoff=0)
            self.PullDownMenu_TxTopics_MenuButton["menu"] = self.PullDownMenu_TxTopics_MenuButton.menu
            self.PullDownMenu_TxTopics_MenuButton.menu.add_command(label="Create new")
            self.PullDownMenu_TxTopics_MenuButton.menu.add_command(label="Open")
            self.PullDownMenu_TxTopics_MenuButton.grid(row=3, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
            '''
            #########################################################

        self.PullDownMenu_TxTopics.grid(row=3, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.PuttyEquivTextContent=[]
        self.PuttyEquivTextContent.insert(int(0), StringVar())
        self.PuttyEquivTextContent_default_text = "Enter command to transmit over MQTT."
        self.PuttyEquivTextInputBox = Entry(self.myFrame, width=50,  textvariable=self.PuttyEquivTextContent[0], state="normal", justify='left')
        self.PuttyEquivTextInputBox.grid(row=4, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        self.PuttyEquivTextContent[0].set(self.PuttyEquivTextContent_default_text)
        self.PuttyEquivTextInputBox.bind('<Return>', lambda event, name = "<Return>": self.PuttyEquivButtonResponse(event, name))
        self.PuttyEquivTextInputBox.bind('<Button-1>', lambda event, name = "<Button-1>": self.PuttyEquivButtonResponse(event, name))
        self.PuttyEquivTextInputBox.bind('<Button-2>', lambda event, name = "<Button-2>": self.PuttyEquivButtonResponse(event, name))
        self.PuttyEquivTextInputBox.bind('<Button-3>', lambda event, name = "<Button-3>": self.PuttyEquivButtonResponse(event, name))
        self.PuttyEquivTextInputBox.bind('<Leave>', lambda event, name = "<Leave>": self.PuttyEquivButtonResponse(event, name))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.PrintToGui_Label = Label(self.myFrame, text="PrintToGui_Label", width=150)
        if self.EnableInternal_MyPrint_Flag == 1:
            self.PrintToGui_Label.grid(row=5, column=0, padx=1, pady=1, columnspan=10, rowspan=10, sticky="w")
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.GUI_ready_to_be_updated_flag = 1
        #########################################################
        #########################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PullDownMenu_TxTopics_CallbackFunction(self, event = None, name = "default"):

        print("PullDownMenu_TxTopics_CallbackFunction event = '" + str(name) + "' fired!")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PuttyEquivButtonResponse(self, event = None, name = "default"): #Have it accept 1 event argument for when it gets binded to Enter Key and Mouse Click

        if name == "<Button-1>" or name == "<Button-2>" or name == "<Button-3>":
            self.PuttyEquivTextContent[0].set("")

        elif name == "<Leave>" and self.PuttyEquivTextContent[0].get() == "": #If the mouse pointer leaves the widget
            self.PuttyEquivTextContent[0].set(self.PuttyEquivTextContent_default_text)
            self.root.focus_set() #Gets the keyboard icon out of the widget

        elif name != "<Leave>":
            MessageToBeTransmitted = self.PuttyEquivTextContent[0].get()
            #self.MyPrint_WithoutLogFile("MessageToBeTransmitted: " + MessageToBeTransmitted)

            self.PuttyEquivTextContent[0].set("")


            ########################
            if sys.version_info[0] < 3:  # Python2

                curselection = self.PullDownMenu_TxTopics.curselection()
                if len(curselection) > 0: #empy if nothing selected
                    TxTopicFromPulldownMenu_LocalCopy = self.PullDownMenu_TxTopics.get(curselection)
                else:
                    TxTopicFromPulldownMenu_LocalCopy = self.MQTT_Tx_topic_list[0]

            else: #Python 3
                TxTopicFromPulldownMenu_LocalCopy = self.PullDownMenu_TxTopics_StrVar.get()

            #print("TxTopicFromPulldownMenu_LocalCopy: " + str(TxTopicFromPulldownMenu_LocalCopy))
            ########################


            QOS_CorrespondingTo_TxTopicFromPulldownMenu_LocalCopy = 2 #Most conservative be default in case we can't find the matching value
            for counter, value in enumerate(self.MQTT_Tx_topic_list):
                if value == TxTopicFromPulldownMenu_LocalCopy:
                    QOS_CorrespondingTo_TxTopicFromPulldownMenu_LocalCopy = self.MQTT_Tx_QOS_list[counter]
                    #print("PuttyEquivButtonResponse, found a QOS match!")

            self.AddDataToBeSent(TxTopicFromPulldownMenu_LocalCopy, MessageToBeTransmitted, QOS_CorrespondingTo_TxTopicFromPulldownMenu_LocalCopy)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_update_clock(self):

        #######################################################
        #######################################################
        #######################################################
        if self.USE_GUI_FLAG == 1 and self.EXIT_PROGRAM_FLAG == 0:

            #######################################################
            #######################################################
            if self.GUI_ready_to_be_updated_flag == 1:

                #######################################################
                self.MQTT_Rx_Label["text"] = "RxMessageCounter: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.MostRecentRxMessageDict["RxMessageCounter"], 0, 3)  + \
                                            "\nRxMessageTimeSeconds: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.MostRecentRxMessageDict["RxMessageTimeSeconds"], 0, 3) + \
                                            "\nRxMessageTopic: " + self.MostRecentRxMessageDict["RxMessageTopic"] + \
                                            "\nRxMessageData: " + self.MostRecentRxMessageDict["RxMessageData"] + \
                                            "\nRx Freq: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_CalculatedFromRxThread, 0, 3) + \
                                            "\nRx Queue Length: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.MQTT_RxMessage_Queue.qsize(), 0, 3)
                #######################################################

                #######################################################
                self.MQTT_Tx_Label["text"] = "TxMessageCounter: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.MostRecentTxMessageDict["TxMessageCounter"], 0, 3)  + \
                                            "\nTxMessageTimeSeconds: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.MostRecentTxMessageDict["TxMessageTimeSeconds"], 0, 3) + \
                                            "\nTxMessageTopic: " + self.MostRecentTxMessageDict["TxMessageTopic"] + \
                                            "\nTxMessageData: " + self.MostRecentTxMessageDict["TxMessageData"] + \
                                            "\nTx Freq: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_CalculatedFromTxThread, 0, 3) + \
                                            "\nTx Queue Length: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.MQTT_TxMessage_Queue.qsize(), 0, 3)
                #######################################################

                #######################################################
                self.PrintToGui_Label.config(text = self.PrintToGui_Label_TextInput_Str)
                #######################################################

        #######################################################
        #######################################################
        #######################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def MyPrint_WithoutLogFile(self, input_string):

        input_string = str(input_string)

        if input_string != "":

            #input_string = input_string.replace("\n", "").replace("\r", "")

            ################################ Write to console
            # Some people said that print crashed for pyinstaller-built-applications and that sys.stdout.write fixed this.
            # http://stackoverflow.com/questions/13429924/pyinstaller-packaged-application-works-fine-in-console-mode-crashes-in-window-m
            if self.PrintToConsoleFlag == 1:
                sys.stdout.write(input_string + "\n")
            ################################

            ################################ Write to GUI
            self.PrintToGui_Label_TextInputHistory_List.append(self.PrintToGui_Label_TextInputHistory_List.pop(0)) #Shift the list
            self.PrintToGui_Label_TextInputHistory_List[-1] = str(input_string) #Add the latest value

            self.PrintToGui_Label_TextInput_Str = ""
            for Counter, Line in enumerate(self.PrintToGui_Label_TextInputHistory_List):
                self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + Line

                if Counter < len(self.PrintToGui_Label_TextInputHistory_List) - 1:
                    self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + "\n"
            ################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IsInputList(self, InputToCheck):

        result = isinstance(InputToCheck, list)
        return result
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

        number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

        ListOfStringsToJoin = []

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if isinstance(input, str) == 1:
            ListOfStringsToJoin.append(input)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
            element = float(input)
            prefix_string = "{:." + str(number_of_decimal_places) + "f}"
            element_as_string = prefix_string.format(element)

            ##########################################################################################################
            ##########################################################################################################
            if element >= 0:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
                element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
            else:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
            ##########################################################################################################
            ##########################################################################################################

            ListOfStringsToJoin.append(element_as_string)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, list) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append(self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, tuple) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append("TUPLE" + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, dict) == 1:

            if len(input) > 0:
                for Key in input: #RECURSION
                    ListOfStringsToJoin.append(str(Key) + ": " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a dict()
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        else:
            ListOfStringsToJoin.append(str(input))
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if len(ListOfStringsToJoin) > 1:

            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            StringToReturn = ""
            for Index, StringToProcess in enumerate(ListOfStringsToJoin):

                ################################################
                if Index == 0: #The first element
                    if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                        StringToReturn = "{"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                        StringToReturn = "("
                    else:
                        StringToReturn = "["

                    StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
                ################################################

                ################################################
                elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                    StringToReturn = StringToReturn + StringToProcess + ", "
                ################################################

                ################################################
                else: #The last element
                    StringToReturn = StringToReturn + StringToProcess

                    if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                        StringToReturn = StringToReturn + "}"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                        StringToReturn = StringToReturn + ")"
                    else:
                        StringToReturn = StringToReturn + "]"

                ################################################

            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

        elif len(ListOfStringsToJoin) == 1:
            StringToReturn = ListOfStringsToJoin[0]

        else:
            StringToReturn = ListOfStringsToJoin

        return StringToReturn
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertDictToProperlyFormattedStringForPrinting(self, DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

        ProperlyFormattedStringForPrinting = ""
        ItemsPerLineCounter = 0

        for Key in DictToPrint:

            ##########################################################################################################
            if isinstance(DictToPrint[Key], dict): #RECURSION
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                     Key + ":\n" + \
                                                     self.ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

            else:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                     Key + ": " + \
                                                     self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)
            ##########################################################################################################

            ##########################################################################################################
            if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
                ItemsPerLineCounter = ItemsPerLineCounter + 1
            else:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
                ItemsPerLineCounter = 0
            ##########################################################################################################

        return ProperlyFormattedStringForPrinting
    ##########################################################################################################
    ##########################################################################################################

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


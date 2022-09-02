########################  

MQTT_ReubenPython2and3Class

Code for sending and receiving data via MQTT (including text and images), with the ability to hook to a Tkinter GUI.

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision E, 08/29/2022

Verified working on: 

Python 2.7, 3.8.

Windows 8.1, 10 64-bit

Raspberry Pi Buster 

(no Mac testing yet)

To test with your own MQTT server, run two instances of "test_program_for_MQTT_ReubenPython2and3Class.py" like this:

python test_program_for_MQTT_ReubenPython2and3Class.py -i 0

python test_program_for_MQTT_ReubenPython2and3Class.py -i 1

When you type a message to send in 1 instance, the other will receive it (and vice versa).

########################  

########################### Python module installation instructions, all OS's

MQTT_ReubenPython2and3Class, ListOfModuleDependencies: ['future.builtins', 'paho.mqtt.client']

MQTT_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['MyPrint_ReubenPython2and3Class']

MQTT_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['future.builtins']

MQTT_ReubenPython2and3Class, ListOfModuleDependencies_All: ['future.builtins', 'MyPrint_ReubenPython2and3Class', 'paho.mqtt.client']

"sudo pip install paho-mqtt" works on windows (without sudo) and Raspberry Pi

###########################

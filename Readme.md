# FSM generator  for arduino based on Moore machine

This version what thinked to be a helper to learn embedded development and discover the event/callback 

state machine are represented threw 2 functions transition and entry

transition represent the comportment of state when an event is cached these function are callbacked

entry represent actions made when an event involve a new state 

actions are performed on states following Moore state machine
# Execution Installation :

### python 3.5:
```
apt install python3.5
```
### pip 3 :
python library amanager
```
apt install python3-pip
```
#### may have to update pip
```
pip3 install --upgrade pip
```

### untangle:
scxml parser for python 
```
pyp3 install untangle
```
### arduino ide :
check at https://www.arduino.cc/en/main/software


### MsTimer2 
required for clock automation

The folder is avaliable inside arduino_runner it have to be copy inside arduino sketchbook libraries to be able to compile and televerse the code on the arduino 

default arduino sketchbook folder :
```
cp -r arduino_runner/MsTimer2 ~/sketchbook/libraries
```
# Generate the finite state machine
### execute the generator
```
python3.5 generator.py [-f FLIENALE]
```
default file fsm.xml
### Generated files
 files with _new must be renamed the first time and later used to compare what is new to not lose data manually entered as function definition

#### fsm.h 
headers for the application that doesn't need to be modified

#### fsm_new.cpp
this is the file where the finite state machine is describe 
you must add the work inside the different function (minimun the TODO)


#### output_new.ino 
is the main file for arduino you must rename it the same as the folder of the application

you may add some elements inside the setting to add peripherals and so on

the loop function shall not have to be modified

#### layout.h 
header file where you have to specify inputs for interruption event

#### params_new.h
header file where you have to specify the clocks details

check that the nubber 

# Lunch all tests :
### execute the test luncher
```
./test_lancher.sh
```
# Run the application
after have done the installation of all the requirement describe on top

execute the generator with the scxml file (default fsm.xml)

copy the file generated inside output directory into arduino_runner/arduino_app

remove all the _new inside the files generated

add your code inside fsm.cpp and give the parameters inside params.h and layout.h
(files filled avaliable inside arduino_runner/arduino_app/example_fillwith_print )

instead you can compare both files to validate that I have only add some Serial.println() (with meld for example)

use arduino ide to compile televerse (for the example one button in digit 2 is requested)
and serial monitor for result
# Functionality avaliable 

##### The generator allows to generate finite state machine from scxml file with
 
 - _transition send event_ name analyser to add physical interrupt as button (eventName_KINDofALERT_interrupt)
 - _transition send internal event_ allowing loop call without exiting state (no onentry done)
 - _onentry_ analysed to generate function involving actions 
 - _onentry_ with _transition interal_ call the event with a specific _delay_ in ms
 - _initial_ find as a argument or as a node 
 - take a file in execution or find the fsm.xml by default
 - generate file to be filled named FILE_new.(h|cpp|ino) allowing to use them by renaming them but not erase previous work
 

##### The generator does not generate finite state machine with (non Exhaustively)
 
 - _hierarchic_ state
 - _parallel_ state because of the non efficiency of executing thread on arduino uno with the arduino overlay
 - _raise_ because of the untangle that chain the node and raise is a world reserved of python
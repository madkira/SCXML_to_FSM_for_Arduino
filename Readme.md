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
###execute the test luncher
```
./test_lancher.sh
```


# Functionality avaliable 

The generator allows to generate finite state machine from scxml file with
 
 - _transition send event_ name analyser to add physical interrupt as button (eventName_KINDofALERT_interrupt)
 - _transition send internal event_ allowing loop call without exiting state (no onentry done)
 - _onentry_ analysed to generate function involving actions 
 - _onentry_ with _transition interal_ call the event with a specific _delay_ in ms
 
 

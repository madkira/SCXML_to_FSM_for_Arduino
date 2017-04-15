# FSM generator  for arduino based on Moore machine


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
#### fsm.h 
headers for the application that doesn't need to be modified

#### fsm_required.cpp
this is the file where the finite state machine is describe 
you must add the work inside the different function (minimun the TODO)


#### output_required.ino 
is the main file for arduino you must rename it the same as the folder of the application

you may add some elements inside the setting to add peripherals and so on

the loop function shall not have to be modified

#### layout.h 
header file where you have to specify inputs for interruption event

#### params.h
header file where you have to specify the clocks details

check that the nubber 

# Lunch all tests :
###execute the test luncher
```
./test_lancher.sh
```


# Functionality avaliable 


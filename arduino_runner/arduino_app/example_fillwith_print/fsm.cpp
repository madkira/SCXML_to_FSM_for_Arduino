/******************************************************* 
 *  author    : Raphaël KUMAR generator
 *  copyright : SoFAB CC-BY-SA
 *  file      : fsm_requred.cpp
 *  object    : This is what is needed inside the fsm.cpp file
 ***/
#include "Arduino.h"
#include "layout.h"
#include "clocks.h"
#include "fsm.h"

void (* current_state)(Event) ;

void run_current(Event evt){
   current_state(evt);
}

void call_for_initial_on_entry(){
	current_state = RUN_trans;
	RUN_entry();
}

void RUN_trans(Event evt){
	switch (evt){
	  case Pause_RISING_interrupt:
		Serial.println("Button Interrupt event move From state RUN to PAUSE");
		current_state = PAUSE_trans;
		PAUSE_entry();
		break;
	  case Time:
		Serial.println("Intern event send");
		doUpdate();
		clock_start(SYSTICK_Time_CLOCK, SYSTICK_Time_RECALL_PERIOD, Time);
		break;
	  default: Serial.println("Event not preempted");
	}
}
void RUN_entry(){
	Serial.println("Onentry RUN");
	doRun();
	clock_start(SYSTICK_Time_CLOCK, SYSTICK_Time_ONENTRY_PERIOD, Time);
}
void PAUSE_trans(Event evt){
	switch (evt){
	  case Pause_RISING_interrupt:
		Serial.println("Button Interrupt event move From state PAUSE to RUN");
		current_state = RUN_trans;
		RUN_entry();
		break;
	  default: Serial.println("Event not preempted");
	}
}
void PAUSE_entry(){
	Serial.println("Onentry PAUSE");
	doPause();
}
void doPause(){
    Serial.println("doPause");
	//TODO add your code for the exectuion
}
void doUpdate(){
    Serial.println("doUpdate");
	//TODO add your code for the exectuion
}
void doRun(){
    Serial.println("doRun");
	//TODO add your code for the exectuion
}
void interrupt_Pause_RISING(){
	push_event(Pause_RISING_interrupt);
}

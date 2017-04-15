/******************************************************* 
 *  author    : Raphaël KUMAR generator
 *  copyright : SoFAB CC-BY-SA
 *  file      : arduino_app.ino
 *  object    : the main file of your project
 ***/
#include "MsTimer2.h"
#include "SoftwareSerial.h"
#include "layout.h"
#include "params.h"
#include "systick.h"
#include "noria.h"
#include "clocks.h"
#include "fsm.h"


void setup(){ 
	//todo : add all your setup for your arduino (be careful with generated code)

	pinMode(digit_Pause, INPUT_PULLUP);
	attachInterrupt(interrupt_Pause, interrupt_Pause_RISING, RISING);
	# ifdef TRACE
        Serial.begin(115200);
        Serial.println("Initialisation du system");
    # endif
    noria_init();
    clocks_init();
    systick_init();
    call_for_initial_on_entry();
    systick_start();
}

void loop(){
    Event current = pop_event();
    if (current != NO_EVENT) run_current(current);
}

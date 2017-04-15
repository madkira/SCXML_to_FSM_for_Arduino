#include "layout.h"
#include "params.h"
#include "systick.h"
#include "noria.h"
#include "clocks.h"
#include "fsm.h"


void setup(){
	#todo : add all your setup for your arduino (be careful with generated code)
	call_for_generated_setup();
	call_for_initial_on_entry();
}

void loop(){
	Event current = pop_event();
	if (current != Event.NO_EVENT) current_state(pop_event());
}
/*******************************************************
 *  author    : Jean DEMARTINI
 *  copyright : SoFAB CC-BY-SA
 *  file      : systick.cpp
 *  object    : hardware master clock
 ***/
#include "MsTimer2.h"
#include "systick.h"
#include "clocks.h"

/*** 
 * this function is run in foreground in the ISR of timer2, 
 * then it is necessary to take care about shared variables.
 ***/
void systick(){
  clocks_tick();    // ticking of all the living software clocks at each systick period
}

void systick_init(){
  MsTimer2::set(SYSTICK_PERIOD, systick);
}

void systick_start(){
  MsTimer2::start();
}

/*******************************************************
 *  author    : Jean DEMARTINI
 *  copyright : SoFAB CC-BY-SA
 *  file      : clocks.cpp
 *  object    : software clocks derived from systick
 ***/
#include "Arduino.h"
#include "clocks.h"
#include "noria.h"

Clock_t clocks[CLOCKS_NUMBER];

void 
clock_init(Clock_t *clk){
  clk->tick = 0;          // all clocks are sleeping
  clk->evt  = NO_EVENT;   // the no event
}

int 
clock_count(Clock_t *clk){
  return clk->tick;
}

/*** run in foreground ***/
void 
clock_tick(Clock_t *clk){
  if(clk->tick == 0) return;
	
  clk->tick--;
  if(clk->tick == 0) {
    push_event(clk->evt);
  }
}

void 
clock_start(Clock_t *clk, int t, Event_t e){
  noInterrupts();
  clk->tick = t;
  clk->evt  = e;
  interrupts();
}

void 
clock_reset(Clock_t *clk){
  noInterrupts();
  clk->tick = 0;
  interrupts();
}

void 
clocks_init(){
  int i;

  for(i=0; i<CLOCKS_NUMBER ; i++){ clock_init(&clocks[i]); }
}

void 
clocks_tick(){
  int i;

  for(i=0; i<CLOCKS_NUMBER ; i++){ clock_tick(&clocks[i]); }
}

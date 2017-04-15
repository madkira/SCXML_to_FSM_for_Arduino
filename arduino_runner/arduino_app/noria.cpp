/*******************************************************
 *  author    : Jean DEMARTINI
 *  copyright : SoFAB CC-BY-SA
 *  file      : noria.cpp
 *  object    : the event FIFO queue for a non-preemptive multi-micro-tasks OS
 *
 *  A very simple model:
 *    - the FIFO queue is linear
 *    - the initial state is ip = op = 0
 *    - at each push ip pointer is incremented
 *    - at each pop op pointer is incremented (op is tracking ip till it reaches it)
 *    - when op reaches ip, the ip and op pointers are re-initialized
 *    - if ip reaches the end of the file a crash is signaled
 ***/
#include "Arduino.h"
#include "noria.h"

static Event noria_ribbon[NORIA_RIBBON_SIZE];

Noria_t noria = {
	NORIA_RIBBON_SIZE,
	0, 0,
	noria_ribbon,
};


/*** events queue management functions ***/
void next_ip() { noria.ip++; }
void next_op() { noria.op++; }
int  distio()  { return (noria.ip-noria.op); }

/*** in setup ***/
void noria_init(void) { noria.ip = noria.op = 0; }

/*** in foreground or in background ***/
void
push_event(Event evt) {
  if (distio()  == 0) { noria_init(); }
  
  noria.ribbon[noria.ip] = evt; 
  next_ip();
  if (noria.ip == NORIA_RIBBON_SIZE) {
    Serial.println("event queue overloaded");
    noria_init();
  }
}

/*** always in background ***/
Event
pop_event() {
  if (distio() == 0) { return Event.NO_EVENT; }
 
  /*** critical section - start ***/
  noInterrupts();
  Event_t e = noria.ribbon[noria.op];
  next_op();
  interrupts();
  /*** critical section - end ***/
  return e;
}

/*******************************************************
 *  author    : Jean DEMARTINI
 *  copyright : SoFAB CC-BY-SA
 *  file      : eQueue.h
 *  object    : the event queue for a non-preemptive multi-micro-tasks OS
 ***/
#include "param.h"
#pragma		once

#define NORIA_RIBBON_SIZE	    5


void    noria_init(void);
void    push_event(Event);
Event pop_event(void);

typedef struct noria {
  int size;
  int ip;
  int op;
  Event *ribbon;
} Noria_t;

extern Noria_t noria;

/*** the unique mandatory event ***/
void  NO_EVENT(void);



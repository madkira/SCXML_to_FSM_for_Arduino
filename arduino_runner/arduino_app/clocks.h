/*******************************************************
 *  author    : Jean DEMARTINI
 *  copyright : SoFAB CC-BY-SA
 *  file      : clocks.h
 *  object    : software clocks derived from systick
 ***/
#pragma once

#include "noria.h"


typedef struct clock{
  int      tick;   // current count-down - clock is sleeping if 0
  Event  evt;    // event triggered when count-down reaches 0
} Clock_t;

extern Clock_t clocks[];

void clocks_init(void);
void clocks_tick(void);
void clock_start(Clock_t *, int, Event);
int  clock_count(Clock_t *clk);
void clock_reset(Clock_t *);

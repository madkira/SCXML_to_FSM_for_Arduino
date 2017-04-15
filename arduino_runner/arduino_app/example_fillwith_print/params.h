/******************************************************* 
 *  author    : Raphaël KUMAR generator
 *  copyright : SoFAB CC-BY-SA
 *  file      : params.h
 *  object    : applicative parameters
 ***/

#pragma once

#define TRACE

#define MODEM_BUFFER_SIZE			256

enum Event {Pause_RISING_interrupt, Time, NO_EVENT};


#define SYSTICK_Time_CLOCK					&clocks[0]
#define SYSTICK_Time_ONENTRY_PERIOD			10
#define SYSTICK_Time_RECALL_PERIOD			250  //TODO set the value of the waiting 1 if instant

#define CLOCKS_NUMBER		1

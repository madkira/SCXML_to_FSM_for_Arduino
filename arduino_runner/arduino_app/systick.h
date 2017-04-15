/*******************************************************
 *  author    : Jean DEMARTINI
 *  copyright : SoFAB CC-BY-SA
 *  file      : systick.h
 *  object    : hardware master clock
 ***/
#pragma once

#define SYSTICK_PERIOD           1    // ms

void systick_init(void);
void systick_start(void);

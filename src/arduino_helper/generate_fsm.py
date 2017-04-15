from src.arduino_helper.Grettings import Grettings
from src.arduino_helper.generate_layout import generate_layout
from src.arduino_helper.generate_app_ino import generate_app_ino
from src.arduino_helper.generate_params import generate_params
import re


def generate_fsm(machine):
    fsm_h = open("output/fsm.h", "w")
    fsm_cpp_required = open("output/fsm_new.cpp", "w")
    fsm_h.write(Grettings("fsm.h", "ain applicative fsm"))

    fsm_cpp_required.write(Grettings("fsm_requred.cpp", "This is what is needed inside the fsm.cpp file"))
    fsm_cpp_required.write("#include \"Arduino.h\"\n\
#include \"layout.h\"\n\
#include \"clocks.h\"\n\
#include \"fsm.h\"\n\n\
void (* current_state)(Event) ;\n\n\
void run_current(Event evt){\n\
   current_state(evt);\n\
}\n\n")

    fsm_h.write("\n#pragma once\n\n")
    fsm_h.write("#include \"params.h\"\n")
    fsm_h.write("void run_current(Event evt);\nvoid call_for_initial_on_entry();\n")
    fsm_cpp_required.write("void call_for_initial_on_entry(){\n\tcurrent_state = "+ machine.first + "_trans;\n\t"+ machine.first+"_entry();\n}\n\n")
    all_event=dict()
    interrupt_event=dict()
    to_implement=dict()
    redefined = dict()
    timed_onentry = dict()
    for state in machine.states:
        transition_name= dict()
        onentry_clock=dict()
        for event in state.transition:
            tmp = event.name.split('_')
            if tmp[len(tmp) - 1] == "interrupt": interrupt_event[event.name] = event.name
            transition_name[event.name] = event
        for action in state.onentry:
            if action["event"] not in transition_name :
                tmp = action["event"].split('_')
                if tmp[len(tmp) - 1] == "interrupt": interrupt_event[action["event"]] = action["event"]
                to_implement[action["event"]] = action
            else :
                try:
                    time = get_timer(action["delay"])
                    string = action["event"] + time
                    transition_name[string] = transition_name.pop(action["event"])
                    timed_onentry[action["event"]] = time
                    onentry_clock[action["event"]] = time
                except IndexError:
                    pass

        redefined["void " + state.name + "_trans(Event evt);\n"] = "void " + state.name + "_trans(Event evt);\n"

        fsm_cpp_required.write("void " + state.name + "_trans(Event evt){\n\tswitch (evt){\n")
        for transition in state.transition :
            all_event[transition.name] = transition.name
            fsm_cpp_required.write("\t  case " + transition.name + ":")
            if transition.internal :
                for action in transition.actions :
                    fsm_cpp_required.write("\n\t\t"+ action +"();")
                    to_implement[action] = action
                fsm_cpp_required.write("\n\t\tclock_start(SYSTICK_" + transition.name + "_CLOCK, SYSTICK_" + transition.name+ "_RECALL_PERIOD, " + transition.name+ ");")
            else:
                fsm_cpp_required.write("\n\t\tcurrent_state = "+ transition.state+"_trans;\n\t\t"+ transition.state+"_entry();")
            fsm_cpp_required.write("\n\t\tbreak;\n")
        fsm_cpp_required.write ("\t  default: Serial.println(\"Event not preempted\");\n\t}\n}\n")

        redefined["void " + state.name + "_entry();\n"] = "void " + state.name + "_entry();\n"
        fsm_cpp_required.write("void " + state.name + "_entry(){\n")
        for action in state.onentry:
            if action["event"] in to_implement:
                fsm_cpp_required.write("\t" + action["event"] + "();\n")
        for action in onentry_clock :
            fsm_cpp_required.write("\tclock_start(SYSTICK_"+ action +"_CLOCK, SYSTICK_"+action+"_ONENTRY_PERIOD, "+ action + ");\n")
        fsm_cpp_required.write("}\n")



    for implement in to_implement:
        fsm_h.write("void "+implement +"();\n")
        fsm_cpp_required.write("void "+implement +"(){")
        try:
            fsm_cpp_required.write(to_implement[implement].script)
        except:
            fsm_cpp_required.write("\n\t//TODO add your code for the exectuion\n}\n")

    for redef in redefined:
        fsm_h.write(redef)
    for interrupt in interrupt_event :
        name = interrupt.split('_')
        fsm_h.write("void interrupt_" + name[0] + "_" + name[1] + "();\n")
        fsm_cpp_required.write("void interrupt_" + name[0] + "_" + name[1] + "(){\n\tpush_event("+interrupt+");\n}\n")
    generate_layout(interrupt_event)
    generate_app_ino(interrupt_event)
    generate_params(all_event, timed_onentry)


def get_timer(string):
   return re.compile('\d+', re.IGNORECASE).match(string).group()
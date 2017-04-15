from src.arduino_helper.Grettings import Grettings

def generate_params(events, clocks):
    params_f = open("output/params_new.h", "w")
    params_f.write(Grettings("params_new.h", "applicative parameters"))
    params_f.write("\n#pragma once\n\n#define MODEM_BUFFER_SIZE\t\t\t256\n\n")

    params_f.write("enum Event {")
    for event in events:
        params_f.write(event + ", ")
    params_f.write("NO_EVENT};\n\n")

    i = 0
    for clock in clocks:
        params_f.write("\n#define SYSTICK_"+clock+"_CLOCK\t\t\t\t\t&clocs["+str(i)+"]")
        params_f.write("\n#define SYSTICK_"+clock+"_ONENTRY_PERIOD\t\t\t"+ clocks[clock])
        params_f.write("\n#define SYSTICK_"+clock+"_RECALL_PERIOD\t\t\t//TODO set the value of the waiting 1 if instant\n\n")
        i = i+1

    params_f.write("#define CLOCKS_NUMBER\t\t"+str(i))
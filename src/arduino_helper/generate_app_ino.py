from src.arduino_helper.Grettings import Grettings

def generate_app_ino(layouts):
    ino_f = open("output/output_required.ino", "w")
    ino_f.write(Grettings("output_required.ino", "the main file of your project"))
    ino_f.write('# include "MsTimer2.h"\n# include "SoftwareSerial.h"\n# include "layout.h"\n# include "params.h"\n# include "systick.h"\n# include "noria.h"\n# include "clocks.h"\n# include "fsm.h"\n\n\n')
    ino_f.write("void setup(){ \n\t//todo : add all your setup for your arduino (be careful with generated code)\n\n")
    all = dict()
    for layout in layouts:
        tmp = layout.split('_')
        if tmp[0] not in all:

            all[tmp[0]] = tmp[0]
            ino_f.write("\tpinMode(digit_" + tmp[0] + ", INPUT_PULLUP);\n")
            ino_f.write("\tattachedInterrupt(interrupt_" + tmp[0] + "," + layout + " , " + tmp[len(tmp) - 2] + ");\n")

    ino_f.write("\t# ifdef TRACE\n\
        Serial.begin(115200);\n\
        Serial.println(\"Initialisation du system\");\n\
    # endif\n\
    noria_init();\n\
    clocks_init();\n\
    systick_init();\n\
    call_for_initial_on_entry();\n\
}\n\
\n\
void loop(){\n\
    Event current = pop_event();\n\
    if (current != NO_EVENT) run_current(current);\n\
}\n")
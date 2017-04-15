from src.arduino_helper.Grettings import Grettings

def generate_params(options):
    option_f = open("output/params.h", "w")
    option_f.write(Grettings("params.h", "applicative parameters"))
    option_f.write("\n#pragma once\n\n#define MODEM_BUFFER_SIZE\t\t\t256\n\n")
    for option in options:
        option_f.write("#define digit_"+ option + "\t/***TODO give the pin number***/\n")
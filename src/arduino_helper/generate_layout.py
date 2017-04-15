from src.arduino_helper.Grettings import Grettings

def generate_layout(layouts):
    layout_f = open("output/layout.h", "w")
    layout_f.write(Grettings("layout.h", "hardware layout interruption definition"))
    layout_f.write("\n#pragma once\n\n")
    all = dict()
    for layout in layouts:
        tmp = layout.split('_')[0]
        if tmp not in all :
            all[tmp] = tmp
            layout_f.write("#define digit_"+ tmp + "\t\t\t//pin_number\n")
            layout_f.write("#define interrupt_"+ tmp + "\t\t//interrupt_number\n\n")

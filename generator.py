#!/usr/bin/python
import argparse

from src.SCXML_Parser.Scxml_parsor import Scxml_parsor
from src.arduino_helper.generate_fsm import generate_fsm

parser = argparse.ArgumentParser()

parser.add_argument('-f', action='store', dest='file', type=str, required=False, default="fsm.xml")
inargs = parser.parse_args()

print ("Beginning of the arduino fsm generator")
parser = Scxml_parsor(inargs.file)

generate_fsm(parser)



print("End")
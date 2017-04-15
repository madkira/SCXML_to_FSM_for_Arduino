#!/bin/bash
touch test/__init__.py
touch test/SXML_parser/__init__.py
python3.5 -m unittest discover -s test -p '*_Test.py'
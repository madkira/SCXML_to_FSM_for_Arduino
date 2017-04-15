import unittest

import untangle

from src.SCXML_Parser.State_parsor import State_parsor
from src.exception.State_Error import TrasitionNotFound

class getTransition(unittest.TestCase) :


    def test_get_Trasition_Events(self):
        scxml = State_parsor( untangle.parse("test/xml/getTransition.xml").state)
        self.assertEqual(scxml.obtain_Transition_Event()[0].name, "Lap")
        self.assertEqual(scxml.obtain_Transition_Event()[1].name, "Out")



    def test_Transtition_Not_Present(self):
        scxml = State_parsor(untangle.parse("test/xml/getTransition_notPresent.xml").state)
        with self.assertRaises(TrasitionNotFound ):
            scxml.obtain_Initial(scxml.obtain_Transition_Event())

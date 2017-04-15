import unittest

import untangle

from src.SCXML_Parser.State_parsor import State_parsor
from src.exception.State_Error import OnEntryNotFound


class getOnentry(unittest.TestCase) :


    def test_getEvents(self):
        scxml = State_parsor( untangle.parse("test/xml/getOnentry.xml").state)
        self.assertEqual(scxml.obtain_Onentry_Event()[0]["event"], "doRun")
        self.assertEqual(scxml.obtain_Onentry_Event()[1]["event"], "Time_pin")


    def test_Onentry_Not_Present(self):
        scxml = State_parsor(untangle.parse("test/xml/getOnentry_notPresent.xml").state)
        with self.assertRaises(OnEntryNotFound ):
            scxml.obtain_Initial(scxml.obtain_Onentry_Event())


    def test_Onentry_No_Event(self):
        scxml = State_parsor(untangle.parse("test/xml/getOnentry_empty.xml").state)
        self.assertEqual(scxml.obtain_Onentry_Event(), None)
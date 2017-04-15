import unittest

import untangle

from src.SCXML_Parser.State_parsor import State_parsor
from src.exception.State_Error import InitNotFound


class getInitial(unittest.TestCase) :

    def test_initial_inSCXML(self):
        scxml = State_parsor( untangle.parse("test/xml/getInitial_inSCXML.xml").scxml)
        self.assertEqual(scxml.obtain_Initial(), 'INIT')

    def test_initial_inNODE(self):
        scxml = State_parsor(untangle.parse("test/xml/getInitial_inNODE.xml").scxml)
        self.assertEqual(scxml.obtain_Initial(), 'INIT')

    def test_no_inital(self):
        scxml = State_parsor(untangle.parse("test/xml/getInitial_ERROR.xml").scxml)
        with self.assertRaises( InitNotFound):
            scxml.obtain_Initial()

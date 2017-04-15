import untangle

from src.Data_Model.State import State
from src.SCXML_Parser.State_parsor import State_parsor


class Scxml_parsor(object):

    def __init__(self, file):

        self._tree = untangle.parse(file).scxml

        self._first = State_parsor(self._tree).obtain_Initial()
        self._states = []

        for state in self._tree.state :
            st_parse = State_parsor(state)
            self._states.append(st_parse.obtain_state())


    @property
    def first(self):
        return self._first

    @property
    def states(self):
        return self._states


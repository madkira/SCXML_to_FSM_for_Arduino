from src.exception.State_Error import *
from src.Data_Model.State import State
from src.Data_Model.Event import Event
from src.SCXML_Parser.Event_parsor import Event_parsor


class State_parsor(object):

    def __init__(self, state):
        self._tree = state


    def obtain_state(self):
        return State(self.obtain_name(), self.obtain_Transition_Event(), self.obtain_Onentry_Event())

    def obtain_name(self):
        try:
            return self._tree["id"]
        except IndexError:
            pass
    def obtain_Initial(self):
        first = None
        try :
            first = self._tree["initial"]
        except IndexError :
            pass
        if first is None:
            try:
                first = self._tree.initial.transition["target"]
            except IndexError:
                pass
        if first is None :
            raise InitNotFound("Error No ititial state found")
        return first


    def obtain_Onentry_Event(self):
        try: self._tree.onentry
        except IndexError:
            raise OnEntryNotFound("Error No onEntry found")
        try:
            return self._tree.onentry.send
        except IndexError:
            return None

    def obtain_Transition_Event(self):
        try: self._tree.transition
        except IndexError:
            raise TrasitionNotFound("Error No trasition found")
        try:
            events = []
            for event in self._tree.transition :
                events.append(Event_parsor(event).obtain_event())
            return events
        except IndexError:
            return None
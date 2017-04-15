
from src.Data_Model.Event import Event


class Event_parsor(object):

    def __init__(self, event):
        self._event = event


    def obtain_event(self):
        return Event(self.obtain_name(), self.obtain_state(), self.obtain_actions(), self.is_internal(),)


    def is_internal(self):
        try:
            return True if self._event["type"] == "internal" else False
        except IndexError:
            return False

    def obtain_name(self):
        try:
            return self._event["event"]
        except IndexError:
            return None #raise

    def obtain_state(self):
        try :
            return self._event["target"]
        except IndexError :
            return None #raise


    def obtain_actions(self):
        try: self._event.send
        except IndexError:
            return None
        try:
            actions = []
            for action in self._event.send:
                actions.append(action["event"])
            return actions
        except IndexError:
            return None  #raise
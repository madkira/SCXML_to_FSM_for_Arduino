from src.Data_Model import State


class Event(object):
    def __init__(self, name, state, actions=None, internal=False):
        self._name = name
        self._state = state
        self._actions = actions
        self._internal = internal


    @property
    def state(self):
        return self._state

    @property
    def name(self):
        return self._name


    @property
    def actions(self):
        return self._actions


    @property
    def internal(self):
        return self._internal
from src.Data_Model import Event


class State(object):
    def __init__(self, name, transitions = None, onentries= None, children = None):
        self._name=name
        self._children=[]
        self._transitions=[]
        self._onentry=[]
        if children is not None:
            for child in children:
                self.add_child(child)
        if transitions is not None :
            for transition in transitions :
                self._transitions.append(transition)
                #self.add_transition(transition)
        if onentries is not None:
            for onentry in onentries:
                self._onentry.append(onentry)
                #self.add_onentry(onentry)



    @property
    def name(self):
        return self._name


    @property
    def chlidren(self):
        return self._children

    @property
    def onentry(self):
        return self._onentry

    @property
    def transition(self):
        return self._transitions


    def add_child(self, node):
        assert isinstance(node, State)
        self.children.append(node)

    def add_transition(self, transition):
        assert isinstance(transition, Event)
        self._transitions.append(transition)

    def add_onentry(self, onentry):
        assert isinstance(onentry, Event)
        self._onentry.append(onentry)
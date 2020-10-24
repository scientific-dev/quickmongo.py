# Import Util
from .Util import AttrDict

# Import Erros
from .Exception import InvalidEventError

class Events():

    def __init__(self, events: dict):
        self.events = events

        for key in events.keys():
            if not callable(events[key]):
                raise InvalidEventError('event provided for ' + str(key) + 'is an inavlid event')

    def emit(self, name, arg = None):
        if name in self.events.keys():
            try:
                if not arg:
                    self.events[name]()
                else:
                    self.events[name](arg)
            except TypeError:
                raise InvalidEventError('provided event for ' + str(name) + ' has invalid amount of parameter or has an error inside the function')

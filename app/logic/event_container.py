
class EventContainer:
    def __init__(self, event):
        self.event = event

    def __lt__(self, other):
        try:
            return self.event.time < other.event.time
        except AttributeError:
            return NotImplemented

    def __gt__(self, other):
        try:
            return self.event.time > other.event.tim
        except AtttributeError:
            return NotImplemented

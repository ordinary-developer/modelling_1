from abc import ABCMeta, abstractmethod


class Event(metaclass=ABCMeta):

    def __init__(self, time):
        self.time = time

    def __lt__(self, other):
        try:
            return self.time < other.time
        except AttributeError:
            return NotImplemented

    def __gt__(self, other):
        try:
            return self.time > other.time
        except AtttributeError:
            return NotImplemented

    @abstractmethod
    def handle_self(self, Model):
        pass

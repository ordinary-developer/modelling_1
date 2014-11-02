from abc import ABCMeta, abstractmethod

class Event(metaclass=ABCMeta):

    def __init__(self, time):
        self.set_time(time)

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    time = property(get_time, set_time, None, None)

    @abstractmethod
    def handle_self(self, model):
        pass

from abc import ABCMeta, abstractmethod

class Event(metaclass=ABCMeta):

    def __init__(self, time):
        self.time = time

    def get_time(self):
        return self.__time
    def set_time(self, time_value):
        self.__time = time_value
    time = property(get_time, set_time, None, None)

    @abstractmethod
    def handle_self(self, model):
        pass

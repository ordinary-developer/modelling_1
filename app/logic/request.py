class Request:

    def __init__(self,number, time):
        self.number = number
        self.time = time

    def get_number(self):
        return self.__number
    def set_number(self, number):
        self.__number = number
    number = property(get_number, set_number, None, None) 

    def get_time(self):
        return self.__time
    def set_time(self, time_value):
        self.__time = time_value
    time = property(get_time, set_time, None, None)

    
    

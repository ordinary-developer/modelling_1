from collections import deque
import random

class Device:

    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
        self.request_queue = deque()
        self.next_request_number = 0
        self.present_request = None

    # [properties]
    def get_first_value(self):
        return self.__first_value
    def set_first_value(self, first_value):
        self.__first_value = first_value
    first_value = property(get_first_value, set_first_value, None, None)

    def get_second_value(self):
        return self.__second_value
    def set_second_value(self, second_value):
        self.__second_value = second_value
    second_value = property(get_second_value, set_second_value, None, None)

    def get_request_queue(self):
        return self.__request_queue
    def set_request_queue(self, request_queue):
        self.__request_queue = request_queue
    request_queue = property(get_request_queue, set_request_queue, None, None)

    def get_next_request_number(self):
        return self.__next_request_number
    def set_next_request_number(self, next_request_number):
        self.__next_request_number = next_request_number
    next_request_number = property(get_next_request_number,
            set_next_request_number, None, None)

    def get_present_request(self):
        return self.__present_request
    def set_present_request(self, present_request):
        self.__present_request = present_request
    present_request = property(get_present_request, set_present_request,
            None, None)

    #[logic]
    def get_processing_time(self):
        r = random.random()
        return self.first_value + (self.second_value - self.first_value) * 4

    def add_request(self, request):
        self.request_queue.append(request)

    def remove_request(self):
        return self.request_queue.popleft()

    def is_empty_request_queue(self):
        return len(self.request_queue) == 0

from queue import PriorityQueue
import math
import random
from app.logic.incoming_event import IncomingEvent
from app.logic.outcoming_event import OutcomingEvent
from app.logic.device import Device
from app.logic.request import Request
from app.logic.event_container import EventContainer

class Model:
    #static fields
    work_time = None
    interval_time = None
    event_list = None
    model_time = None

    @staticmethod
    def initialize(work_time_value):
        Model.work_time = work_time_value
        Model.model_time = 0
        Model.interval_time = 60
        Model.event_list = PriorityQueue()
        Model.add_event(IncomingEvent(0.0))
        Model.device = Device(30, 70)

    @staticmethod
    def start():
        while Model.model_time < Model.work_time:
            (time, present_event) = Model.get_event()
            Model.model_time = present_event.time
            present_event.handle_self(Model)

    @staticmethod
    def add_event(event):
        Model.event_list.put((event.time, EventContainer(event)))

    @staticmethod
    def get_event():
        (time, event_container) = Model.event_list.get()
        return (time, event_container.event)
    
    @staticmethod
    def get_exp_interval():
        return (-1) * math.log(1 - random.random()) * Model.interval_time

    @staticmethod
    def handle_incoming_event(time):
        event_time = time + Model.get_exp_interval()
        Model.add_event(IncomingEvent(event_time))
        current_request_number = Model.device.next_request_number
        request = Request(current_request_number, time)
        if Model.device.present_request != None:
            Model.device.add_request(request)
        else:
            Model.process_device(request)

        print('[handle an incoming event]\t\t{0} sec.'.format(event_time))

    @staticmethod
    def handle_outcoming_event(time):
        Model.device.present_request = None
        if not Model.device.is_empty_request_queue():
            request = Model.device.remove_request()
            Model.process_device(request)
        else:
            Model.device.present_request = None

        print('[handling an outcoming event]\t\t{0} sec.'.format(time))

    @staticmethod
    def process_device(request):
        Model.device.present_request = request
        Model.device.next_request_number += 1
        time = Model.device.get_processing_time()
        total_time = Model.model_time - request.time
        Model.add_event(OutcomingEvent(Model.model_time + total_time))

        print('[processing the device]\t\t\trequest #{0}'.format(request.number))

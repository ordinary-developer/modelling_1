from queue import PriorityQueue
import math
import random
from app.logic.incoming_event import IncomingEvent
from app.logic.device import Device

class Model:
    #static fields
    work_time = None
    interval_time = None
    event_list = None
    model_time = None

    @staticmethod
    def initialize(work_time_value):
        Model.work_time = work_time_value
        Model.interval_time = 60
        Model.event_list = PriorityQueue()
        Model.addEvent(IncomingEvent(0))
        Model.device = Device(30, 70)

    @staticmethod
    def addEvent(event):
        Model.event_list.put(int(event.time), event) 
    
    @staticmethod
    def get_exp_interval():
        return (-1) * math.log(1 - random.random()) * Model.interval_time


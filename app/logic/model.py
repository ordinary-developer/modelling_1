from queue import PriorityQueue
from app.logic.incoming_event import IncomingEvent

class Model:
    #static fields
    work_time = None
    event_list = None

    @staticmethod
    def initialize(work_time_value):
        Model.work_time = work_time_value
        Model.event_list = PriorityQueue()
        Model.addEvent(IncomingEvent(0))

    @staticmethod
    def addEvent(event):
        Model.event_list.put(event) 
    

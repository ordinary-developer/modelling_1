from app.logic.event import Event
#from app.logic.model import Model


class IncomingEvent(Event):

    #[abstract method implementation]
    def handle_self(self, Model):
        Model.handle_incoming_event(self.time)

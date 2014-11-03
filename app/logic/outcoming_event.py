from app.logic.event import Event
#from app.logic.model import Model


class OutcomingEvent(Event):

    #[abstract method implementation]
    def handle_self(self, Model):
        Model.handle_outcoming_event(self.time)

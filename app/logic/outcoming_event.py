from app.logic.event import Event


class OutcomingEvent(Event):

    #[abstract method implementation]
    def handle_self(self, Model):
        Model.handle_outcoming_event(self.time)

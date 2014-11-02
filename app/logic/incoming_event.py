from app.logic.event import Event


class IncomingEvent(Event):

    #[abstract method implementation]
    def handle_self(self, model):
        pass

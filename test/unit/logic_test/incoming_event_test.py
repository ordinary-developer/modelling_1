import unittest
from app.logic.incoming_event import IncomingEvent

class TestIncomingEvent(unittest.TestCase):

    def setUp(self):
        self.time = 10.0
        self.incoming_event = IncomingEvent(self.time)

    def test_create_incoming_event_with_correct_time(self):
        self.assertAlmostEqual(self.time, self.incoming_event.time)

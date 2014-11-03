import unittest
from app.logic.model import Model
from app.logic.request import Request

class TestModel(unittest.TestCase):

    def setUp(self):
        self.work_time = 8 * 60 * 60
        Model.initialize(self.work_time)

    def test_initialize_model_with_correct_time(self):
        self.assertAlmostEqual(self.work_time, Model.work_time, delta = 0.005)

    def test_create_event_list_not_none(self):
        self.assertIsNotNone(Model.event_list)

    def test_initialize_model_with_event_adding(self):
        self.assertEqual(1, Model.event_list.qsize())

    def test_initialize_model_with_device_adding(self):
        self.assertIsNotNone(Model.device)

    def test_initialize_model_with_not_zero_exp_intervale(self):
        self.assertGreater(Model.get_exp_interval(), 0)

    def test_handle_incoming_event(self):
        #[ARRANG]
        self.time = 10.5
        #[ACT]
        Model.handle_incoming_event(self.time)
        #[ASSERT]
        self.assertGreater(Model.event_list.qsize(), 0)

    def test_handle_process_device(self):
        #[ARRANGE]
        time = 11.5
        request_number = 5
        request = Request(request_number, time)

        old_next_request_number = Model.device.next_request_number
        #[ACT]
        Model.process_device(request)
        #[ASSERT]
        self.assertIsNotNone(Model.device.present_request)
        self.assertGreater(Model.device.next_request_number,
                old_next_request_number)


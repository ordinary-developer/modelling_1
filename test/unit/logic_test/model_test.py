import unittest
from app.logic.model import Model

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


from unittest import TestCase, main

from Python_OOP.Testing.Lab.Worker.worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker('TestWorker', 25000, 100)

    def test_correct_initialization(self):

        self.assertEqual('TestWorker', self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_method_if_no_exception(self):
        self.worker.work()
        self.assertEqual(25000, self.worker.money)
        self.assertEqual(99, self.worker.energy)

    def test_wor_method_exception(self):
        self.worker.energy = 0 # arrange

        with self.assertRaises(Exception) as ex: # act
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception)) # assert

    def test_rest_method(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info_method(self):
        self.assertEqual('TestWorker has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
import unittest
import unittest.mock

from main import starting_hour_input, ending_hour_input, babysitter_payment_calculator


class Tests(unittest.TestCase):

    @unittest.mock.patch('builtins.input', side_effect=[5])
    def test_5_pm_is_zero_for_starting(self, input):
        assert starting_hour_input() == 0

    @unittest.mock.patch('builtins.input', side_effect=[6])
    def test_6_pm_is_first_hour_for_starting(self, input):
        assert starting_hour_input() == 1

    @unittest.mock.patch('builtins.input', side_effect=[9])
    def test_9_pm_is_fourth_hour_for_starting(self, input):
        assert starting_hour_input() == 4

    @unittest.mock.patch('builtins.input', side_effect=[9])
    def test_9_pm_is_fourth_hour_for_ending_for_starting(self, input):
        assert ending_hour_input() == 4

    @unittest.mock.patch('builtins.input', side_effect=[4])
    def test_4_am_is_eleventh_hour_for_ending(self, input):
        assert ending_hour_input() == 11

    def test_work_for_all_hours_max_pay(self):
        self.assertEqual(136, babysitter_payment_calculator(0, 11))

    def test_start_and_end_on_same_hour_pay(self):
        self.assertAlmostEqual(0, babysitter_payment_calculator(4, 4))


if __name__ == '__main__':
    unittest.main()

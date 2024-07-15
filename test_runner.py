import unittest
from runner import Runner

class TestRunner(unittest.TestCase):
    def test_runner_initialization(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        
        # Check the initialization of attributes
        self.assertEqual(runner.name, 'Elijah')
        self.assertEqual(runner.age, 18)
        self.assertEqual(runner.country, 'Australia')
        self.assertEqual(runner.sprint_speed, 5.8)
        self.assertEqual(runner.endurance_speed, 4.4)
        self.assertEqual(runner.energy, 1000)

    def test_runner_initialization_invalid_1(self):
        # Test initialization with invalid age (greater than 120)
        with self.assertRaises(CustomValueError):
            Runner('Tim', 121, 'Australia', 6.9, 5.5)

    def test_runner_initialization_invalid_2(self):
        # Test initialization with invalid sprint_speed and endurance_speed
        with self.assertRaises(CustomValueError):
            Runner('Bob', 4, 'Australia', 2.1, 1.7)

    def test_runner_drain_energy_valid(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        # Drain energy by 250 points
        runner.drain_energy(250)
        self.assertEqual(runner.energy, 750)

    def test_runner_drain_energy_excessive(self):
        runner = Runner('Tim', 55, 'Australia', 5.5, 5.3)
        # Drain energy by 900 points, should leave 100 points
        runner.drain_energy(900)
        self.assertEqual(runner.energy, 100)

    def test_runner_drain_energy_minimal(self):
        runner = Runner('Bob', 35, 'Australia', 4.5, 3.5)
        # Drain minimal energy by 1 point
        runner.drain_energy(1)
        self.assertEqual(runner.energy, 999)

    def test_runner_recover_energy_valid(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        runner.drain_energy(250)
        # Recover energy by 200 points
        runner.recover_energy(200)
        self.assertEqual(runner.energy, 950)

    def test_runner_recover_energy_to_max(self):
        runner = Runner('Tim', 55, 'Australia', 5.5, 5.3)
        runner.drain_energy(500)
        # Attempt to recover more than max energy, should cap at 1000
        runner.recover_energy(1001)
        self.assertEqual(runner.energy, 1000)

    def test_runner_recover_energy_minimal(self):
        runner = Runner('Bob', 35, 'Australia', 4.5, 3.5)
        runner.drain_energy(2)
        # Recover minimal energy by 1 point
        runner.recover_energy(1)
        self.assertEqual(runner.energy, 999)

    def test_runner_run_race_long(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        # Run a long race of 5 km
        time_taken = runner.run_race("long", 5.0)
        self.assertEqual(time_taken, 1136.36)

    def test_runner_run_race_short(self):
        runner = Runner('Tim', 55, 'Australia', 5.5, 5.3)
        # Run a short race of 5 km
        time_taken = runner.run_race("short", 5.0)
        self.assertEqual(time_taken, 909.09)

    def test_runner_run_race_invalid_type(self):
        runner = Runner('Bob', 35, 'Australia', 4.5, 3.5)
        # Test invalid race type
        with self.assertRaises(CustomValueError):
            runner.run_race("medium", 5.0)

if __name__ == '__main__':
    unittest.main()

import unittest
from autompg import AutoMPGData
import random
print("This is autompg_test:", __name__)

class TestAutoMPG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass")
    cls.auto_data = AutoMPGData()

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass")
        clean_file = "auto-mpg.clean.txt"
        if os.path.exists(clean_file):
            os.remove(clean_file)

    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("\ntearDown")

    def test_str(self):
        print("\nExecuting test_str.")
        random_cars = random.sample(self.auto_data.data, 3)
        for car in random_cars:
            self.assertTrue(str(car).startswith("AutoMPG("))

    def test_eq(self):
        print("\nExecuting test_eq.")
        car1, car2 = random.sample(self.auto_data.data, 2)
        if car1 == car2:
            self.assertEqual(hash(car1), hash(car2))
        else:
            self.assertNotEqual(car1, car2)

    def test_lt(self):
        print("\nExecuting test_lt.")
        subset = random.sample(self.auto_data.data, 4)
        sorted_subset = sorted(subset)
        for i in range(len(sorted_subset) - 1):
            self.assertTrue(sorted_subset[i] < sorted_subset[i+1])

    def test_hash(self):
        print("\nExecuting test_halt.")
        random_cars = [random.choice(self.auto_data.data) for _ in range(5)]
        unique_cars_set = set(random_cars)
        self.assertTrue(len(unique_cars_set) >= 1)


if __name__ == "__main__":
    unittest.main()

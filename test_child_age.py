import unittest
from age import categorize_by_age

class TestIschild(unittest.TestCase):
    
    def test_is_child(self):
        for age in range(150):
            with self.subTest(age=age):
                try:
                    self.assertEqual(categorize_by_age(age), "Child")
                    print(f"\n{age} is categorized as a Child.")
                except AssertionError:
                    continue

    def test_is_adult(self):
        for age in range(150):
            with self.subTest(age=age):
                try:
                    self.assertEqual(categorize_by_age(age), "Adult")
                    print(f"\n{age} is categorized as an Adult.")
                except AssertionError:
                    continue

    def test_is_golden(self):
        for age in range(150):
            with self.subTest(age=age):
                try:
                    self.assertEqual(categorize_by_age(age), "Golden")
                    print(f"\n{age} is categorized as a Golden.")
                except AssertionError:
                    continue


if __name__ == "__main__":
    unittest.main(verbosity=1)
import unittest
from age import categorize_by_age

class TestIschild(unittest.TestCase):
    
    def test_child_age(self):
        for age in range(150):
            print(f"\n{age} is considered as a child.")
            try:
                self.assertEqual(categorize_by_age(age), "Child")
            except:
                break

if __name__ == "__main__":
    unittest.main(verbosity=2)
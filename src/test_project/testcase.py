import unittest


def add(num1, num2):
    return num1 + num2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(3, add(1, 1))


if __name__ == '__main__':
    unittest.main()

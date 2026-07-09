import unittest

from app import add, greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_message(self) -> None:
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_strips_whitespace(self) -> None:
        self.assertEqual(greet("  Ada  "), "Hello, Ada!")

    def test_greet_rejects_empty_name(self) -> None:
        with self.assertRaises(ValueError):
            greet("   ")


class TestAdd(unittest.TestCase):
    def test_add_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_add_floats(self) -> None:
        self.assertAlmostEqual(add(1.5, 2.25), 3.75)


if __name__ == "__main__":
    unittest.main()

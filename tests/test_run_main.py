"""Tests that the main module of the get_me_food module can be imported and ran."""
import unittest


from get_me_food import __main__


class TestMain(unittest.TestCase):
    """Tests that the main module of the get_me_food module can be imported and ran."""

    def test_run_main(self):
        """Tests the import and successful call of the main module."""
        __main__.main(["--ingredients", "tomato", "olive", "salmon"])

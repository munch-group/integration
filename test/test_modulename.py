import unittest

from integration.modulename import functionname

class TestModulename(unittest.TestCase):

    def test_functionname(self):
        self.assertEqual(
            functionname(
                1, 1
                ),
                2
            )

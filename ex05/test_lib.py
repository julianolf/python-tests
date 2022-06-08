import sys
import unittest

from . import lib


class TestLib(unittest.TestCase):
    @unittest.skip("Something is broken here")
    def test_does_something_wrong(self):
        self.assertEqual(lib.does_something_wrong(), 2)

    @unittest.skipIf(lib.__version__ >= (2, 0), "version not supported")
    def test_do_something(self):
        self.assertEqual(lib.do_something(), "done")

    @unittest.skipUnless(not sys.platform.startswith("darwin"), "OS not supported")
    def test_fails_on_mac(self):
        self.failIf(sys.platform.startswith("darwin"), "On MacOS")

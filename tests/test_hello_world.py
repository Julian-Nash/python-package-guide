from helloworld import HelloWorld

import unittest


class TestReader(unittest.TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_reader_function(self):

        hw = HelloWorld(name="Foo Bar")
        msg = hw.say_hello()

        self.assertEqual(msg, "Hello Foo Bar!!")
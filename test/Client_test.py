import unittest

from service.client import Client


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = Client('mock name', 'mock last', '')

    def test_name_last_name(self):
        expected_name = 'mock name mock last'
        self.assertEqual(self.test_client.get_formatted_name(), expected_name)

    def test_name_add_preexistence(self):
        self.assertEqual(len(self.test_client.get_all_preexistence()), 0)

        self.test_client.add_preexistence('mock preexistence')
        self.assertEqual(len(self.test_client.get_all_preexistence()), 1)

        self.assertEqual(self.test_client.get_preexistence(0), 'mock preexistence')
        self.assertEqual(self.test_client.get_preexistence(1), 'There is no such preexistence')

    def test_name_remove_preexistence(self):
        self.assertEqual(len(self.test_client.get_all_preexistence()), 0)

        self.test_client.add_preexistence('mock preexistence')
        self.test_client.add_preexistence('mock preexistence 2')
        self.test_client.add_preexistence('mock preexistence 3')
        self.assertEqual(len(self.test_client.get_all_preexistence()), 3)
        self.test_client.remove_preexistence(1)
        self.assertEqual(len(self.test_client.get_all_preexistence()), 2)
        self.assertEqual(self.test_client.get_preexistence(0), 'mock preexistence')
        self.assertEqual(self.test_client.get_preexistence(1), 'mock preexistence 3')
        self.assertEqual(self.test_client.get_preexistence(2), 'There is no such preexistence')


if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    # python -m unittest discover -s test -p "*_test.py"
    # https://stackoverflow.com/questions/11241781/python-unittests-in-jenkins

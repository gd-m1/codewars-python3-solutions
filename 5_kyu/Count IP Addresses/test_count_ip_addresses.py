import unittest

from count_ip_addresses import ips_between


class Test(unittest.TestCase):
    def test_ips_between(self):
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)


if __name__ == '__main__':
    unittest.main()

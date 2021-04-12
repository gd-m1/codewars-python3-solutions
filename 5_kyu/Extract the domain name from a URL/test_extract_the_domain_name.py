import unittest

from extract_the_domain_name import domain_name


class Test(unittest.TestCase):
    def test_extract_the_domain_name(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")


if __name__ == '__main__':
    unittest.main()

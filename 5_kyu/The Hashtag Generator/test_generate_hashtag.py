import unittest

from generate_hashtag import generate_hashtag


class Test(unittest.TestCase):
    def test_generate_hashtag(self):
        self.assertEqual(generate_hashtag(''), False)
        self.assertEqual(generate_hashtag('Do We have A Hashtag')[0], '#')
        self.assertEqual(generate_hashtag('Codewars'), '#Codewars')
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars')
        self.assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice')
        self.assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice')
        self.assertEqual(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice')
        self.assertEqual(generate_hashtag('c i n'), '#CIN')
        self.assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice')
        self.assertEqual(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False)


if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from api import format_url

class TestFormatUrl(unittest.TestCase):
    def test_bon_url(self):
        self.assertEqual(format_url("https", "google.com", "/fr"), "https://google.com/fr")
        self.assertEqual(format_url("http", "example.com", "test"), "http://example.com/test")

    def test_sans_slash(self):
        self.assertEqual(format_url("https", "site.com", "page"), "https://site.com/page")

    def test_sans_uri(self):
        self.assertEqual(format_url("https", "site.com", ""), "https://site.com/")

    def test_format_url_invalid_protocol(self):
        with self.assertRaises(ValueError):
            format_url("ftp", "site.com", "/page")

    def test_sans_hostname(self):
        with self.assertRaises(ValueError):
            format_url("https", "", "/page")
    
    def test_protocol_non(self):
        with self.assertRaises(ValueError):
            format_url(None, "site.com", "/page")

    

if __name__ == "__main__":
    unittest.main()

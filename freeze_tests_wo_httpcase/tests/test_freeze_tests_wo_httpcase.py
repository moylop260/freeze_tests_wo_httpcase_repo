# -*- coding: utf-8 -*-

import unittest
import odoo.tests

try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen


@odoo.tests.at_install(False)
@odoo.tests.post_install(True)
class TestNoFreezeWHttpCase(odoo.tests.HttpCase):
    def test_open_url(self):
        "Testing that opening a non-static url with HttpCase is good!"
        urlopen('http://localhost:8069/web/login')


class TestFreezeWoHttpCase(odoo.tests.TransactionCase):
    @unittest.skip("Disable it if you want to see a testing freeze")
    def test_open_url(self):
        "Testing that before start odoo entirely is not available to use non-static url without HttpCase"
        urlopen('http://localhost:8069/web/login')

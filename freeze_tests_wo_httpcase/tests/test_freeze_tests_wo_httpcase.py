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
    def test_01_open_static_url(self):
        "Testing that opening a static url with HttpCase is good!"
        urlopen('http://localhost:8069/web/static/src/css/reset.min.css')

    def test_02_open_non_static_url(self):
        "Testing that opening a non-static url with HttpCase is good!"
        urlopen('http://localhost:8069/web/login')


class TestFreezeWoHttpCase(odoo.tests.TransactionCase):
    def test_01_open_static_url(self):
        "Testing that a static url is available before to start odoo entirely without HttpCase"
        urlopen('http://localhost:8069/web/static/src/css/reset.min.css')

    @unittest.skip("Disable it if you want to see a testing freeze")
    def test_02_open_non_static_url(self):
        "Testing that a non-static url is not available before to start odoo entirely without HttpCase"
        urlopen('http://localhost:8069/web/login')

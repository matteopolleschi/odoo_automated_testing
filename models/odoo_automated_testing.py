# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo_automated_testing(models.Model):
    _name = 'odoo_automated_testing.odoo_automated_testing'

    name = fields.Char(string='Test Module')
    result = fields.Char(string='Test result')
    test01 = fields.Char(string='Test 1')
    test02 = fields.Char(string='Test 2')
    test03 = fields.Char(string='Test 3')
    test04 = fields.Char(string='Test 4')
    test05 = fields.Char(string='Test 5')
    test06 = fields.Char(string='Test 6')
    test07 = fields.Char(string='Test 7')
    test08 = fields.Char(string='Test 8')
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Odoo_automated_testing(models.Model):
    _name = 'odoo_automated.testing'
    _description = "Odoo automated testing"

    name = fields.Char(string='Test Module', required=True)
    test_ids = fields.One2many('odoo_automated.testing.test', 'testing_module', string='Tests')
    result = fields.Text(string='Results')

    @api.model
    def test_create_invoice_record(self):
        # Add record in test module
        Module_invoicing = self.env['odoo_automated.testing'].create({'name': 'Invoicing'})
        # Add a test customer to the invoice
        test_invoice_customer = self.env['res.partner'].create({'name': 'ExampleCustomer'})
        # Add a test product to the invoice
        category = self.env['product.category'].search([('name', '=', 'All')])
        test_invoice_product = self.env['product.product'].create({'name': 'ExampleProduct','type': 'consu','categ_id': category.id,'lst_price': 50})
        # Create a new invoice with the test
        test_invoice = self.env['account.invoice'].create({'name': 'Testinvoice', 'partner_id': test_invoice_customer.id, 'product_id': test_invoice_product.id})
        # Check if the invoice name, the customer name and product name match
        tests = []
        if test_invoice_customer.name == 'ExampleCustomer':
            tests.append((0, 0, {'description': 'Test if the Customer is created', 'result': True}))
        if test_invoice_product.name == 'ExampleProduct':
            tests.append((0, 0, {'description': 'Test if the Product is created', 'result': True}))
        if test_invoice.name == 'Testinvoice':
            tests.append((0, 0, {'description': 'Test if the Invoice is created', 'result': True}))
        # Check if the invoice untaxed amount, tax and total match
        if test_invoice.amount_untaxed == 50:
            tests.append((0, 0, {'description': 'Test if the Untaxed Amount is 50', 'result': True}))
        if test_invoice.amount_tax == 11:
            tests.append((0, 0, {'description': 'Test if the Tax Amount is 11', 'result': True}))
        if test_invoice.amount_total == 61:
            tests.append((0, 0, {'description': 'Test if the Total amount is 61', 'result': True}))
        # Check if the customer and product added in the invoice are in fact the correct ids
        if test_invoice_customer.id == test_invoice.partner_id:
            tests.append((0, 0, {'description': 'Test if the Customer assinged to the invoice is the correct one', 'result': True}))
        if test_invoice_product.id == test_invoice.product_id:
            tests.append((0, 0, {'description': 'Test if the Product assigned to the invoice is the correct one', 'result': True}))
        # Trasnsfer test result to the table test module field results
        Module_invoicing.write({'test_ids': tests, 'result': 'The test was succesfull!'})
        # Delete all records created in invoice module for testing
        test_invoice_customer.unlink()
        test_invoice_product.unlink()
        test_invoice.unlink()


class Odoo_automated_testing_test(models.Model):
    _name = 'odoo_automated.testing.test'
    _description = "Odoo automated test"

    name = fields.Char(string='Test name', readonly=True, required=True, copy=False, default='New')
    description = fields.Char(string='Test Description', required=True)
    result = fields.Boolean(string='Result')
    testing_module = fields.Many2one('odoo_automated.testing', ondelete='cascade', string='Module')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('odoo_automated.testing.test') or 'New'
        test = super(Odoo_automated_testing_test, self).create(vals)
        return test

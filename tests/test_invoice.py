# -*- coding: utf-8 -*-

from odoo.tests import TransactionCase


class InvoiceTest(TransactionCase):

    def test_create_invoice_record(self):
        # Add a test customer to the invoice and check it
        test_invoice_customer = self.env['res.partner'].create({'name': 'ExampleCustomer'})
        self.assertEqual(test_invoice_customer.name, 'ExampleCustomer')
        # Add a test product to the invoice and check it
        category = self.env['product.category'].search([('name', '=', 'All')])
        test_invoice_product = self.env['product.product'].create(
            {'name': 'ExampleProduct', 'type': 'consu', 'categ_id': category.id, 'lst_price': 50})
        self.assertEqual(test_invoice_product.name, 'ExampleProduct')
        # Create a new invoice and check it
        test_invoice = self.env['account.move'].create(
            {'name': 'Testinvoice', 'partner_id': test_invoice_customer.id, 'product_id': test_invoice_product.id})
        self.assertEqual(test_invoice.name, 'Testinvoice')
        self.assertEqual(test_invoice.amount_untaxed, 50)
        self.assertEqual(test_invoice.amount_tax, 11)
        self.assertEqual(test_invoice.amount_total, 61)
        self.assertEqual(test_invoice_customer.id, test_invoice.partner_id)
        self.assertEqual(test_invoice_product.id, test_invoice.product_id)
        # Do a little print to show it visually for this demo - in production you don't really need this.
        print('The test was succesfull!')

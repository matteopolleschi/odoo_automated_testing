# -*- coding: utf-8 -*-
 
from odoo.tests import common
 
class test_invoice(common.TransactionCase):
    def test_create_data(self):
        # Add a test customer to the invoice
        test_invoice_customer = self.env['res.partner'].create({'name': 'ExampleCustomer'})

        # Add a test product to the invoice
        category = self.env['product.category'].search([('name', '=', 'All')])
        test_invoice_product = self.env['product.product'].create({'name': 'ExampleProduct','type': 'consu','categ_id': category.id,'lst_price': 50})

        # Create a new invoice with the test
        test_invoice = self.env['account.invoice'].create({'name': 'Testinvoice', 'partner_id': test_invoice_customer.id, 'product_id': test_invoice_product.id})
 
        # Check if the invoice name, the customer name and product name match
        test01 = self.assertEqual(test_invoice_customer.name, 'ExampleCustomer')
        self.env['test_invoice_module.test_invoice_module'].create({'test01': 'Create Customer:' + test01})
        test02 = self.assertEqual(test_invoice_product.name, 'ExampleProduct')
        self.env['test_invoice_module.test_invoice_module'].create({'test02': 'Create Product:' + test02})
        test03 = self.assertEqual(test_invoice.name, 'Testinvoice')
        self.env['test_invoice_module.test_invoice_module'].create({'test03': 'Create Invoice:' + test03})

        # Check if the invoice untaxed amount, tax and total match
        test04 = self.assertEqual(test_invoice.amount_untaxed, 50)
        self.env['test_invoice_module.test_invoice_module'].create({'test04': 'Untaxed Amount Correct:' + test04})
        test05 = self.assertEqual(test_invoice.amount_tax, 11)
        self.env['test_invoice_module.test_invoice_module'].create({'test05': 'Tax Correct:' + test05})
        test06 = self.assertEqual(test_invoice.amount_total, 61)
        self.env['test_invoice_module.test_invoice_module'].create({'test06': 'Total Correct:' + test06})

        # Check if the customer and product added in the invoice are in fact the correct ids
        test07 = self.assertEqual(test_invoice_customer.id, test_invoice.partner_id)
        self.env['test_invoice_module.test_invoice_module'].create({'test07': 'Right Customer in Invoice:' + test07})
        test08 = self.assertEqual(test_invoice_product.id, test_invoice.product_id)
        self.env['test_invoice_module.test_invoice_module'].create({'test08': 'Right Product in Invoice:' + test08})

        # Trasnsfer test result to the table test module field results
        self.env['test_invoice_module.test_invoice_module'].create({'result': 'The test was succesfull!'})
        print('Your test was succesfull!')
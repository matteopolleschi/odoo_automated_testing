# -*- coding: utf-8 -*-
{
    'name': "Odoo automated testing",

    'summary': """Odoo Automated Testing Module""",

    'description': """
        This Module test the invoice module features:
            - create an invoice
            - check the invoice content (taxes)
            - create the related e-invoice file
    """,

    'author': "Mounir lahsini",
    'website': "https://github.com/matteopolleschi/odoo_automated_testing",

    'category': 'Hidden',
    'version': '1.0',

    'depends': ['base', 'account'],
    'data': [
        #'security/ir.model.access.csv',
        'views/odoo_automated_testing_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
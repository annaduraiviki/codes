
# -*- coding: utf-8 -*-
{
    'name': "carmanufacturer",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Trainee D.ANNADURAI app 2016
    """,

    'author': "Annadurai",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/noupd.xml',
        'data/noupd.xml',
        'views/carpartsview.xml'
#        'data/carmanufact2.carmanufact2.csv',
#          'data/dat.xml',      
        
    ],
    # only loaded in demonstration mode
   
}
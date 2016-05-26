from openerp import models, fields, api

class landline(models.Model):
    _name='customer.car'
    
    _inherit='customer.car'
    
    landline_number=fields.Char(size=14,string="Landline Number ")
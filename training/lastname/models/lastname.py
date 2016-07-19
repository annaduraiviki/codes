from openerp import models, fields, api

class lastname(models.Model):
    _name='customer.car'
    
    _inherit='customer.car'
    
    cus_last_name=fields.Char(size=1,string="Last Name Initial ")
    
    
    @api.onchange('cus_last_name')
    def onchange_lastname(self):
        self.cus_last_name=str(self.cus_last_name or '').upper()
    
    
    
from openerp import models, fields, api

class saleinherit(models.Model):
    _name='res.partner'
    
    _inherit='res.partner'
    
    sale_percentage=fields.Float(size=14,string="Percentage")
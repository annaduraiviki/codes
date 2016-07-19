from openerp import models, fields, api

class customercustom(models.Model):
    _name='suppliercustom.vms'
    
    _inherit='supplier.car'
    
    supplier_fax=fields.Char(size=14,string="Supplier FAX")
    customer_id=fields.Many2one('customercustom.vms',string="CustomerID")
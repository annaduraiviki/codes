from openerp import models, fields, api

class customercustom(models.Model):
    _name='customercustom.vms'
    
    _inherit='customer.car'
    
    customer_fax=fields.Char(size=14,string="FAX")
    supplier_id=fields.One2many('suppliercustom.vms','customer_id',string="Supplier details")
    
    @api.one
    @api.depends('car_regstate','car_regnumber','car_reginfo')
    def _car_state_number(self):
        if self.car_regnumber ==0 :
            self.car_reginfo= str(self.car_regstate)+  "   02  " +str(self.car_regnumber)
        else:
            self.car_reginfo= str(self.car_regstate)+  " 03 " +str(self.car_regnumber)
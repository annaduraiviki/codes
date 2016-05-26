from openerp import models,fields,api

class service(models.Model):
    
    _name ='service.vechicle'
    
    id=fields.Integer(string="USER ID")
    car_model_name=fields.Many2one('production.vechicle',string="CarMODEL")
    partname=fields.Char(string="Part name")
    state=fields.Char(string="State")
    parts_available=fields.One2many('carparts.vechicle','products_availability',string="Parts here")
    totparts=fields.Integer(string="Total parts")
    costprice=fields.Float(string="Cost price")
    service_charge=fields.Float(string="Service charge")
    totcost=fields.Float(compute='_tot_cost',string="TOTAL COST")
    
    
    @api.one
    @api.depends('totparts','costprice','service_charge','totcost')
    def _tot_cost(self):
            self.totcost=(self.costprice * self.totparts)+self.service_charge
    
    
from openerp import models,fields,api

class carparts(models.Model):
    
    _name='carparts.vechicle'
    
    id=fields.Integer(string="USER ID")
    car_model_name=fields.Many2one('production.vechicle',string="CarMODEL")
    light_model=fields.Selection([('l1','Headlight'),('l2','TailLight'),('l3','InteriorLight')])
    tyres=fields.Selection([('m','MRF'),('m2','Michellin'),('b','Bridgestone')])
    seater=fields.Selection([('leath','leatherCushion'),('ord','ordinaryCushion')])
    products_availability=fields.Many2many('service.vechicle',string="products availability")
from openerp import models,fields,api

class production(models.Model):
    
    _name='production.vechicle'
    _rec_name="id"
    
    id=fields.Integer(string="car ID")
    carmanufacturer=fields.Char(string="Manufacturer", default='FORD', readonly= True)
    carmodel=fields.Selection([('punto','PUNTO'),('fiego','Fiego'),('gt','MUSTANGGT')],string="Car model")
    register_number=fields.Integer(string="Register Number")
    service=fields.One2many('service.vechicle','car_model_name',string="Service")
    parts=fields.One2many('carparts.vechicle','car_model_name',string="parts")
    manufacturing_date=fields.Datetime(string="Manufacturing date")
    mrp=fields.Float(string="MRP")
    tax=fields.Float(string="Tax")
    total_cost=fields.Float(string="TOTAL COST")
    
    
 #   carmodel= fields.Selection([('bmwA1','BMW"A"'),('bmwB1','BMW"B"'),('bmwC1','BMW"C"'),('fordF','FordFiesta'),('fordM','fordMustang'),('fordFF','FordFiego'),('hund1','i10'),('hund2','i20'),('tata1','TATA NANO'),('tata2','Indica'),('Lamb','Lamborgini'),('porsche','Porsche')],String="Car Model")
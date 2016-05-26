from openerp import models,fields,api

class companymanage(models.Model):
    
    _name='comapany.car'
    
    id=fields.Integer(string="Id")
    manufacturer=fields.Many2one('customer.car',string="MANUFACTURER", default="FORD",readonly=True)
    
#    car_model=fields.Selection([('fi','Fistea'),('en','endeavour'),('gt','MUSTANG GT')],string="CAR MODEL")
#    car_regnumber=fields.Char(String="REGISTER NUMBER")
#    manager_name= fields.Selection([('a','popyee'),('v','pluto')],string="Manager")
#    attendence=fields.Selection([('pr','present'),('ab','absent')],string="Attendence")
#    address=fields.Text(string="Adddress")
    
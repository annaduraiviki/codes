from openerp import models,fields,api

class carmanumain3(models.Model):
    
    _name='carmanufact3.carmanufact3'
#    _rec_name= 'carmodel'
    
    
    id=fields.Integer(string="USER ID")
    name1= fields.Many2one('carmanufact0.carmanufact0',string="Car name")
    nameofparts1=fields.Char(string="PartsName")
    state=fields.Char()
    carmodelname=fields.Many2many('carmanufact0.carmanufact0')
#     progress= fields.float('progress', readonly=True, help='Shows you the progress made today on the reconciliation process') 
    
# class carmanumain4(models.Model):
#     
#     _name=    
from openerp import models,fields,api

class carmanumain2(models.Model):
    
    _name='carmanufact2.carmanufact2'
    
    
    id=fields.Integer(string="USER ID")
    name= fields.Char()
    age=fields.Char()
    state=fields.Many2one('carmanufact0.carmanufact0',string="state")
#     progress= fields.float('progress', readonly=True, help='Shows you the progress made today on the reconciliation process') 
    
    
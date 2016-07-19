from openerp import models,fields,api


class stud1(models.Model):
    
    _name='stu'
    _inherits={'stu2':'name'}
    
   # name=fields.Many2one('stu2',"Delegation field NAME")
    age=fields.Integer()
    state=fields.Char()
    name=fields.Many2one('stu2',"Delegation field NAME")
    
class stud2(models.Model):
    
    _name='stu2'
    _rec_name='city'
    
    stu_id=fields.Integer()
    
    city=fields.Char()
    phone=fields.Integer()
    mail=fields.Char()
    gender=fields.Char()    

    
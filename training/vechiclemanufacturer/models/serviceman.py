from openerp import models,fields,api

class servicemanage(models.Model):
    
    _name='service.car'
    #_inherits={'comapany.car':'serviceman_name'}
    _rec_name='serviceman_name'
    
    serviceman_id=fields.Integer(string="Servicemen ID")
    serviceman_name=fields.Char(size=15,string="serviceMan")
    serviceman_address=fields.Text(string="Service man Address")
    salary=fields.Float(string="Salary")
    experience=fields.Integer(string="Years of experience")
    service_cost=fields.Integer(string="Service Cost")
    leave_details=fields.One2many('leave.company','companyleave_id',string="Leave Details",readonly=True)
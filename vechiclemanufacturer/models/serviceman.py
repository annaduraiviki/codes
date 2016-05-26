from openerp import models,fields,api

class servicemanage(models.Model):
    
    _name='service.car'
    
    id=fields.Integer(string="ServiceMan Id")
    serviceman_name=fields.Char(string="serviceMan")
    serviceman_address=fields.Text(string="Service man Address")
    salary=fields.Float(string="Salary")
    experience=fields.Integer(string="Years of experience")
    
    service_cost=fields.Integer(string="Service Cost")
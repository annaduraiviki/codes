
from openerp import models, fields, api
from openerp.exceptions import Warning
from datetime import datetime, timedelta

class personal_details(models.Model):
	_name = 'personal.details'
	
	name = fields.Char(string="Name")
	age = fields.Float()
	date_of_birth =  fields.Date()
	end_date =  fields.Date()
	gender= fields.Selection([('m','Male'), ('f','Female')], 'Gender')
	address= fields.Text()
	email= fields.Char()
	contact= fields.Char()

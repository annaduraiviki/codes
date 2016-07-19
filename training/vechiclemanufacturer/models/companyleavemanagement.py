from openerp import models,fields,api
from datetime import datetime,date
from dateutil.relativedelta import relativedelta 
from dateutil import relativedelta as rdelta
from datetime import date

class companyleaves(models.Model):
    
    _name='leave.company'
        
    companyleave_id=fields.Many2one('service.car',string="company leave")
    leave_type=fields.Many2many('leave.reason',string="Leave type")
    leave_reason=fields.Text(string="Leave Reason")
    from_date=fields.Date()
    to_date=fields.Date()
    total_days=fields.Integer(compute="calculate_date1",string="Total Days")
    
    @api.one
    @api.depends('to_date','from_date')
    def calculate_date1(self):
        
        if self.from_date and self.to_date:
                
            d3 = datetime.strptime(self.from_date, '%Y-%m-%d')
            d4 = datetime.strptime(self.to_date, '%Y-%m-%d')
            self.total_days=abs((d4-d3).days)
            
class leavereason(models.Model):
    
    _name='leave.reason'
    _rec_name="leave_type"
    
    leave_type=fields.Char(string="Leave Type")
    max_leave_take=fields.Integer(string="Maximum leave available")
                
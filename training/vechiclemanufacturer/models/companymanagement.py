from openerp import models,fields,api
from datetime import timedelta
from datetime import datetime,date
from dateutil.relativedelta import relativedelta 
from dateutil import relativedelta as rdelta
from datetime import date


class companymanage(models.Model):
    
    _name='comapany.car'
    _rec_name='id'
    _inherits={'service.car':'serviceman_nameinadmin'}
    _inherit=['mail.thread']
    
    id=fields.Integer(string="Id")
    #serviceman_nameincustomer=fields.Many2one('customer.car',string="Service man in customer")
    serviceman_nameinadmin=fields.Many2one('service.car',string="Service Man Name")
    admin_name=fields.Char(string="AdminName",default="ADMIN", readonly=True)
    admin_phonenumber=fields.Char(size=10,string="Admin phone number")
    cust_id=fields.Many2one('customer.car',string="CUSTOMER ID")
    from_date=fields.Date(string="Register date", required=True)
    final_date=fields.Date(string="Last date",required=True)
    total_days=fields.Integer(compute="calculate_date",string="TOTAL DAYS")
    follwers_id=fields.Integer('follwers_id')
    followers_msg=fields.Integer('msg',track_visibility='always')
    admin_access=fields.Char(string="ADMIN ACCESS",help="Give Code to access this form for adding customer")
    
    
    @api.model
    def create(self,vals):
        if vals['admin_phonenumber'] == '98':
            vals['admin_phonenumber']='9839283025'
        return super(companymanage, self).create(vals)  
    
    @api.one
    @api.depends('final_date','from_date')
    def calculate_date(self):
        
        if self.from_date and self.final_date:
                
            d3 = datetime.strptime(self.from_date, '%Y-%m-%d')
            d4 = datetime.strptime(self.final_date, '%Y-%m-%d')
            self.total_days=abs((d4-d3).days)
            
            
            #self.total_days = rdelta.relativedelta(d3,d4).days    # it is also working
             
           
#             d1=datetime.strptime(str(self.from_date),'%y-%m-%d')
#             print d1
#         
#             d2=datetime.strptime(str(self.final_date),'%y-%m-%d')
#             
#             self.total_days=str((d2-d1).days)
#         
        #self.final_date=datetime.strptime(self.from_date)
        #rd=relativedelta(d2-d1)
            
        #self.final_date=vals['']
        
        #d1=datetime.strptime(self.from_date)
        #d2=datetime.strptime(self.final_date)
        #self.total_days=datetime.strptime(self.from_date - self.final_date)
        
#    @api.onchange('date_of_birth')
#    def _value_pc(self):
#        if(self.date_of_birth):
#            current_day = date.today()
#            bdate = datetime.strptime(self.date_of_birth,'%Y-%m-%d')
#            self.age = relativedelta(current_day ,bdate).years 
    
    
#    car_model=fields.Selection([('fi','Fistea'),('en','endeavour'),('gt','MUSTANG GT')],string="CAR MODEL")
#    car_regnumber=fields.Char(String="REGISTER NUMBER")
#    manager_name= fields.Selection([('a','popyee'),('v','pluto')],string="Manager")
#    attendence=fields.Selection([('pr','present'),('ab','absent')],string="Attendence")
#    address=fields.Text(string="Adddress")
    
from openerp import models,fields,api

class customermanage(models.Model):
    
    _name='customer.car'
    _rec_name='id'
    
    id=fields.Integer(string="Customer Id")
    customer_name=fields.Char(string="CUSTOMER NAME", required=True)
    car_model=fields.Selection([('fi','Fistea'),('en','endeavour'),('gt','MUSTANG GT')],string="CAR MODEL")
    car_regstate=fields.Selection([('py','PONDICHERRY'),('tn','TAMILNADU'),('ke','KERALA')], string="STATE")
    car_regnumber=fields.Char(string=" CAR REGISTER NUMBER",size=4,required=True)
    car_reginfo=fields.Char(compute='_car_state_number',string="REGISTER INFORMATION")
    cus_mobilenumb=fields.Char(size=10,string="CUSTOMER MOBILE NUMBER")
    address=fields.Text(string="CUSTOMER ADDRESS",required=True)
    mailaddress=fields.Char(string="EMAIL - ID")
    total_cost=fields.One2many('supplier.car' ,'cust_id',string="COST INFORMATION")
    customer_avatar=fields.Binary(string="Customer Avatar")
    
    @api.one
    @api.depends('car_regstate','car_regnumber','car_reginfo')
    def _car_state_number(self):
        if self.car_regnumber ==0 :
            self.car_reginfo= str(self.car_regstate)+  "   0 " +str(self.car_regnumber)
        else:
            self.car_reginfo= str(self.car_regstate)+  "  " +str(self.car_regnumber)
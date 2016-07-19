from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning
import re


class customermanage(models.Model): #USE CAMELIN WORDS FOR CLASS
    
    _name = 'customer.car' #Table name
   
    _rec_name = 'id' # For choosing many2one name to another model
   
    id = fields.Integer(string="Customer Id") #fields in table
    customer_name = fields.Char(string="Customer Name", required=True)
    car_model = fields.Selection([('fi', 'Fistea'), ('en', 'endeavour'), ('gt', 'MUSTANG GT')], string="Car Model")   
    car_regstate = fields.Selection([('py', 'PONDICHERRY'), ('tn', 'TAMILNADU'), ('ke', 'KERALA')], string="State")
    car_regnumber = fields.Char(string=" Car Register Number", size=4, required=True) # size="" shows the size of the char or integer length in the field
    car_reginfo = fields.Char(compute='_car_state_number', string="Register Information")
    cus_mobilenumb = fields.Char(size=10, string="Customer Mobile Number")
    address = fields.Text(string="Customer Address", required=True) # if Required is set to TRUE, then the field must be given otherwise it doesnt save the Record
    mailaddress = fields.Char(on_change="ValidateEmail", string="EMAIL - ID")
    total_cost = fields.One2many('supplier.car' , 'cust_id', string="COST INFORMATION")
    customer_avatar = fields.Binary(string="Customer Avatar")# Binary for import Images. Remember if binary field is used Then we have to give Widget= Image in respective field in XML too
    regular_customer = fields.Boolean() # for True or False
    priority = fields.Selection([('0', 'very low'), ('1', 'low'), ('2', 'medium'), ('3', 'high'), ('4', 'very high'), ('5', 'highest')], string="Priority",default='2') # for multiple SELECTIONs
    management = fields.One2many('comapany.car', 'cust_id', string="Customer Management") #just like Relational model in DBMS
    statusbar = fields.Selection([('new', 'New'), ('draft', 'Draft'), ('cancel', 'Cancel'), ('confirm', 'Confirm'), ('done', 'Done')], string="Current status", help="Status if acceptance, Rejection, Confirmation or Cancel ")
    samplefield = fields.Boolean()
    sequence_number = fields.Char(compute="_sequence_number")
    priority_but = fields.Integer(compute="_priority_but", string=" priority count")
    customer_tot_cost = fields.Integer(compute="cust_tot_cost",string="Expenditures")
    amount_total=fields.Float(compute="cust_tot_cost",string="Amount Total") # we may use compute with depends or without depends according to conditions
    percent_bar=fields.Integer(compute="percent_completion",string="In Progress")
    product_quotation=fields.One2many('products.car','customer_id',string="Product quotation") # use for review like things
    review_customer=fields.Text(string="Remarks") 
    deadline_start_date=fields.Date("Start date") #for Date time functionalities
    deadline_end_date=fields.Date("Deadline")
            
    @api.onchange('customer_name')
    def onchange_name(self):
        self.customer_name = str(self.customer_name or '').upper()  # .upper() converts lower string to higher string
    
    @api.one
    @api.depends('statusbar') 
    def percent_completion(self):
        if self.statusbar=='done':
            self.percent_bar=100
        elif self.statusbar=='confirm':
            self.percent_bar=75
        elif self.statusbar=='Draft':
            self.percent_bar=50
        elif self.statusbar=='new':
            self.percent_bar=25      
        elif self.statusbar=='cancel':
            self.percent_bar=10
                
        
    @api.one
    @api.depends('priority')
    def _priority_but(self):
        self.priority_but = self.priority
    
    _sql_constraints = [('car_reginfo_uniq', 'unique(car_regnumber)', 'Register Number must be unique!')] #To perform validation
    _sql_constraints = [('mailadd_uniq', 'unique(mailaddress)', ' Mail address must be unique!')]
    _sql_constraints = [('mobnumb_uniq', 'unique(cus_mobilenumb)', ' Mobile Number must be unique!')]
    
    @api.one
    @api.constrains('customer_name', 'mailaddress')   #check constraints 
    def _check_unique_constraint(self):
        
        if self.priority == False: 
        # if len(self.search(['customer_name', '=', self.customer_name])) > 1: #FOR MY REFERENCE
                raise ValidationError("specify priority")
        if self.mailaddress == False:
                raise Warning("Please specify mail ID")
            
    @api.multi
    @api.constrains('mailaddress') 
    def ValidateEmail(self):
        for partner in self:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", partner.mailaddress) == None: #if re is used then it must be declared in IMPORT as re,_
                raise Warning("Please specify Valid Email ID")
                return False
        return True
    
    @api.one
    @api.constrains('cus_mobilenumb')
    def validatePhonenumber(self):
        for phone in self:
            if re.match("[0-9]", phone.cus_mobilenumb) == None:
                raise Warning("Mobile number is not valid one, Please specify valid number")
                return False
            return True
            
    @api.one
    @api.constrains('customer_name')
    def validateCustomername(self):
        for cusname in self:
            if re.match('[a-zA-Z]', cusname.customer_name) == None:
                raise Warning("Name You entered contains Numeric values, Use Alphabets in Name")
                return False
            return True
        
    @api.one
    @api.depends('car_model', 'car_reginfo')
    def _sequence_number(self):
        if self.sequence_number:
            print self.car_reginfo
        else:    
            self.sequence_number = str(self.id) + "" + str(self.car_model) + "" + str(self.car_reginfo)           
                           

    @api.one
    @api.depends('car_regstate', 'car_regnumber')
    def _car_state_number(self):
        if self.car_regnumber:
            self.car_reginfo = str(self.car_regstate) + "-01-" + str(self.car_regnumber)

    @api.one
    @api.depends('priority')
    def clear_priority(self):
        
            self.write({'priority':""})
            
    @api.multi
    def cust_tot_cost(self):                       
        res = self.env['supplier.car'].search([('cust_id', '=', self.id)])
        val=0
        for i in res:           
            val= val+i.total_price
        self.amount_total=val    
        self.customer_tot_cost=self.amount_total
        print self.customer_tot_cost   
              
    @api.multi
    def unlink(self): 
        if not self.car_model:
            return super(customermanage,self).unlink()
            return { 'type': 'ir.actions.client', 'tag': 'reload', }
         
        else:
            raise Warning("Can't delete the record, contains car model")           
        
    @api.one
    def new_func(self):
        self.write({'statusbar': 'new', })
 
    @api.one
    def draft_func(self):
        self.write({'statusbar': 'draft'})
 
    @api.one
    def cancel_func(self):
        self.write({'statusbar': 'cancel'})
 
    @api.one
    def confirm_func(self):
        self.write({'statusbar': 'confirm', })
    @api.one
    def done_func(self):
        self.write({'statusbar': 'done', })             

#================
# FOR MY REFERENCE
#++++++++++++++++
# _constraints = [(_validate_email, 'Please enter a valid email address.', ['mailaddress']),]




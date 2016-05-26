# -*- coding: utf-8 -*-


from openerp import models, fields, api, _
from datetime import date
from time import time
from openerp.exceptions import UserError

class warehouse(models.Model):
    _name = 'warehouse.warehouse'

    prodname = fields.Char(string="Product name",required=True)
    prodtype = fields.Selection([("a", "SOAP"), ("b", "TOOTHPASTE"), ("c", "RAZOR"),("d","NOTEBOOKS"),("e","WATCH")])         
    prodsubname = fields.Char(string="Product sub name")
    quantity = fields.Integer(string="Quantity")
    proddescription = fields.Text(string="Product Description", copy=False)
    proddate = fields.Datetime(string="Date of purchase")
    prodquality = fields.Selection([("a", "AQuality"), ("b", "BQualitiy"), ("c", "CQuality")], store=True)
    prodcheck = fields.Boolean(string="CheckIt in Warehouse", copy=False)
    prodmprice = fields.Float(string="Productmanuprice", help="Product manufacturing price")  
    prodtax = fields.Float(string="Product plus Tax")
    prod_mrp = fields.Float(compute="_value_pc", store=True, default=1.3)
    timee = fields.Date(string="Expiry date")
    prodfulldetails = fields.Text(compute="full_details",store=True)
    images = fields.Binary(string="Image to upload")
    prodreview = fields.Html(string="Review here!")
    warehousemoney = fields.Text(compute="warmoney", store=True)
    proddiscount = fields.Float(string="Discount price", compute="discountprice", store=True)
    afterdiscounts = fields.Float(String="After Discount", compute ="discountcountedprice", store = True)
    sels=fields.Selection('_get_selection')
    
#     @api.one
#     @api.depends('prodtype','sels')
    def _get_selection(self):
        
        return (('choice1', 'This is the choice 1'),('choice2', 'This is the choice 2')) 
#         vals['sels']=vals['prodtype']
#         res = super(warehouse, self).copy(vals)   
#         return res 

      
    
    @api.depends('prodmprice','prodtax', 'quantity')
    def _value_pc(self):
        if self.prodmprice==0 or self.prodtax==0:
            print "Not to be ZERO"
        elif self.prodmprice<=0 :
            print "check the value" 
             
        else:    
            print "final product MRP is" 
            self.prod_mrp = (self.prodmprice + self.prodtax)*self.quantity
            
            
    @api.depends('prodname','prodtype','prod_mrp','proddiscount','afterdiscounts')        
    def full_details(self):
        self.prodfulldetails = 'Product Name-->  ' + str(self.prodname) + ' Product type--> ' + str(self.prodtype) + ' Product MRP-->  ' + str(self.prod_mrp) + ' Product discount--->' + str(self.proddiscount) +'Product after discounted price---->'+ str(self.afterdiscounts)
        
    @api.depends('prod_mrp')
    def  warmoney(self):
        if self.prod_mrp >=10000:
            self.warehousemoney ="purchase over the budget"
        else:
            self.warehousemoney= "purchase is in budget"      
    
    @api.depends('prod_mrp')
    def discountprice(self):
        if self.prod_mrp>=7500:
            self.proddiscount=float(self.prod_mrp)/100*20
            
                    
    @api.depends('prod_mrp','proddiscount')
    def discountcountedprice(self):
        self.afterdiscounts = self.prod_mrp - self.proddiscount
        
        
    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        default['prodtax'] = 20
        return super(warehouse, self).copy(default)    
        
        
        
        
        
        
        
        
#print "ERROR sys malfunction"
#            raise UserError(_('price or tax can"t be Nullvalue'))       
        
        
#from dateutil import relativedelta        
        
# bloodtype=fields.Char("bloody", store=True)
#    timee2=fields.today()       
#               
#    @api.onchange('bloodGroup')
#    def bloody (self): 
#        self.bloodtype=self.bloodGroup
#        print "in bloody"
#         
#      
#     @api.depends('value1')
#     def _value_pc(self):sendgrid python template
#         self.value3 = float(self.value1) * 5
#         print self.value3   

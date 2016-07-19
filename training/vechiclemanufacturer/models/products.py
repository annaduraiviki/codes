from openerp import models,fields,api
import time
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning

class prod_quantity(models.Model):
    _name='products.car'
    _inherits={'productselection.car':'product_name'}#,'countrystate.custom':'state_customfield'}
    #_inherits={'countrystate.custom':'state_customfield'}
    
    _inherit=['countrystate.custom']
    
    _rec_name="product_name"
    
    product_name=fields.Many2one("productselection.car",string="Product Name")
    qty=fields.Integer(string="Enter Qty")
    customer_id=fields.Many2one("customer.car",string="Customer ID", required=True)
    status=fields.Selection([('new', 'New'), ('draft', 'Draft'), ('cancel', 'Cancel'), ('confirm', 'Confirm'), ('done', 'Done')], string="Current status")
    #date_today=fields.Date(default=date.today())
    #state_customfield=fields.Many2one('countrystate.custom',string="state")
    
    @api.one
    def new_func(self):
        self.write({'status': 'new', })
 

    @api.one
    def draft_func(self):
        self.write({'status': 'draft'})
 

    @api.one
    def cancel_func(self):
        self.write({'status': 'cancel'})
 

    @api.one
    def confirm_func(self):
        self.write({'status': 'confirm', })
    @api.one
    def done_func(self):
        self.write({'status': 'done', })                                                 
         
    
    @api.one
    @api.onchange('qty')
    def onchange_qty(self):
        res=self.env['productselection.car'].search([])
        
        for i in res:
            if i.product_nameselection==self.product_name.product_nameselection:
                val=i.quantity_total-self.qty                    
                i.write({'quantity_total':val})
                    
    @api.constrains('qty','product_name')
    def constrains_qty(self):
        if self.product_name.quantity_total<=self.qty:
            raise Warning("Qty is less then Stored Quantity")  
        
                                                                 
class prod_selection(models.Model):
    
    _name="productselection.car"
    _rec_name="product_nameselection"
        
    product_nameselection=fields.Char(string="Product Name")    
    quantity_total=fields.Integer(string="Total Quantity")
    quantity_button=fields.Integer("Quantities")
    image=fields.Binary(string="Product Image",widget="image")
    
    _sql_constraints = [('prod_name_uniq', 'unique(product_nameselection)', ' Product name already exists')]

    @api.constrains('quantity_total')
    def constaints_quantity(self):
        if self.quantity_total<=0:
            raise Warning(" Bucket is Empty")
    
    @api.one    
    @api.onchange('quantity_total')  
    def quant(self):
        self.quantity_button=self.quantity_total    
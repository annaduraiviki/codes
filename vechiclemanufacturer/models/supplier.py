from openerp import models,fields,api

class suppliermanage(models.Model):
    
    _name='supplier.car'
    
    id=fields.Integer(string="Id")
#    supplier_name=fields.Char(string="customername")
    supplier_name=fields.Selection([('sup','Ford US'),('sup2','FORD UK'),('sup','FORD INDIA')],string="SUPPLIER NAME")
    part_regnumber=fields.Char(String="PART NUMBER")
    parts_Name=fields.Char(string="PARTS NAME")
    date_purchased=fields.Datetime(string="DATE OF PURCHASE")
    product_price=fields.Float(string="PRODUCT PRICE")
    product_quantity=fields.Integer(string="QUANTITY")
    product_tax=fields.Float(string="TAX")
    total_price=fields.Float(compute='_total_price_supplier',string="TOTAL PRICE")
    cust_id=fields.Many2one('customer.car',string="CUSTOMER ID")
    address=fields.Text(string="SUPPLIER ADDRESS")
    
    @api.one
    @api.depends('product_price','product_quantity','product_tax','total_price')
    def _total_price_supplier(self):
        self.total_price=(self.product_price*self.product_quantity)+self.product_tax 
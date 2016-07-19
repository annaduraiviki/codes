from openerp import models,fields,api
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning

class suppliermanage(models.Model):
    
    _name='supplier.car'
    _inherit='countrystate.custom'
    _rec_name='id'
    
    id=fields.Integer(string="Id")
#    supplier_name=fields.Char(string="customername")
    supplier_name=fields.Selection([('sup','Ford US'),('sup2','FORD UK'),('sup3','FORD INDIA')],string="SUPPLIER NAME")
    part_regnumber=fields.Char(String="PART NUMBER")
    parts_Name=fields.Char(string="PARTS NAME")
    date_purchased=fields.Datetime(string="DATE OF PURCHASE")
    product_price=fields.Float(string="PRODUCT PRICE")
    product_quantity=fields.Integer(string="QUANTITY")
    product_tax=fields.Float(string="TAX")
    total_price=fields.Float(compute='_total_price_supplier',string="TOTAL PRICE")
    cust_id=fields.Many2one('customer.car',string="CUSTOMER ID",index=True)
    address=fields.Text(string="SUPPLIER ADDRESS")
    parts=fields.Many2many('partsprovider.vechicle', string="Parts")
    statusbar_custom=fields.Selection([('new','New'),('draft','Draft'),('cancel','Cancel'),('confirm','Confirm'),('done','Done')])
    progress_bar=fields.Integer(compute="progress_completion",string="On Progress")
    total_parts_price=fields.Float(string="Total Amount")
    
    
    @api.multi
    def tot_parts_price(self):
        res=self.env['partsprovider.vechicle'].search([('parts_provider','=',self.id)])
        val=0
        for i in res:
            val=val+i.parts_price
        self.total_parts_price=val    
        print self.total_parts_price
        
    @api.one
    @api.depends('statusbar_custom')
    def progress_completion(self):
        if self.statusbar_custom=='done':
            self.progress_bar=100
            
        elif self.statusbar_custom=='confirm':
            self.progress_bar=75
        elif self.statusbar_custom=='Draft':
            self.progress_bar=50
        elif self.statusbar_custom=='new':
            self.progress_bar=25      
        elif self.statusbar_custom=='cancel':
            self.progress_bar=10
    
    @api.one
    @api.depends('product_price','product_quantity','product_tax','total_price')
    def _total_price_supplier(self):
        self.total_price=(self.product_price*self.product_quantity)+self.product_tax
   
    @api.one   
    def new_func(self):
        self.write({
                    'statusbar_custom': 'new',
         })

    @api.one
    def draft_func(self):
        self.write({
                    'statusbar_custom': 'draft'
        })

    @api.one
    def cancel_func(self):
        self.write({
                    'statusbar_custom': 'cancel'
        })
 
    @api.one
    def confirm_func(self):
        self.write({
                    'statusbar_custom': 'confirm',
                    })
    @api.one
    def done_func(self):
        self.write({
                    'statusbar_custom': 'done',
                    })     
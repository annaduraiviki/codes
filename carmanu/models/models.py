from openerp import models,fields,api
import json

class carmanumain(models.Model):
    
    _name='carmanufact0.carmanufact0'
    _rec_name='companyName'
    
    
    id=fields.Integer(string="USER ID")
    companyName= fields.Char(string="Company Name")
    carmodel= fields.Selection([('bmwA1','BMW"A"'),('bmwB1','BMW"B"'),('bmwC1','BMW"C"'),('fordF','FordFiesta'),('fordM','fordMustang'),('fordFF','FordFiego'),('hund1','i10'),('hund2','i20'),('tata1','TATA NANO'),('tata2','Indica'),('Lamb','Lamborgini'),('porsche','Porsche')],String="Car Model")
    carDescription= fields.Text(string="description")
    carmanuDate= fields.Date(String="Manufacturing Date")
    carmanuPrice=fields.Float (string="MRP")
    carmanuTax= fields.Float(String="TAX")
    carExportTrue= fields.Boolean(string="check")
    carmanuExportPrice = fields.Float(string="Export price")
    carImage= fields.Binary(string="Image")
    carQuantity= fields.Integer(string="Quantity", default=1)
    carTotCost= fields.Float(compute='totcost',string="Total cost", store=True)
    done = fields.Boolean('Done?')
    activee = fields.Boolean('Active?', default=True)
    check =fields.Char()
    work_email=fields.Char(string="Email")
    priority=fields.Selection([ ('0', 'Very Low'),('1', 'Low'),('2', 'Normal'),('3', 'High'),('4', 'Very High')])
    mo=fields.Many2one('carmanufact2.carmanufact2', string="many2one")
    om=fields.One2many('carmanufact2.carmanufact2','state', string="One to many")
    pid3=fields.Many2one('carmanufact0.carmanufact0','pid')
    pid4=fields.One2many('carmanufact3.carmanufact3','name1',string='pidd2')
    category_id= fields.Many2many('res.partner.category')
    cate=fields.Many2many('carmanufact2.carmanufact2')
    

    @api.one
    @api.depends('carmanuPrice','carmanuTax','carmanuExportPrice','carQuantity')
    def totcost(self):
        if self.carQuantity==0:
            self.carTotCost=self.carmanuPrice + self.carmanuTax + self.carmanuExportPrice
 
        else:
            self.carTotCost= (self.carmanuPrice + self.carmanuTax + self.carmanuExportPrice)* self.carQuantity    
#                
    @api.model
    def create(self,vals):
        if not self.carDescription:
            vals['carDescription']='Best to buy'
                         
        res = super(carmanumain, self).create(vals)
#        print "test"
        self.do_clear_done() 
        return  res
#      
    @api.multi
    def write(self,vals):
        if self.companyName=='ford':
            vals['carmanuExportPrice'] = 200
             
#         self.do_clear_done()                                
        res = super(carmanumain, self).write(vals)   
        return res    
#     
#     
    @api.one
    def unlink(self):
        if not self.companyName:
            print "X"
        return super(carmanumain,self).unlink()
#         
    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        default['carmanuTax'] = 20
        res= super(carmanumain, self).copy(default)
        return res
#     
    @api.multi
    def do_clear_done(self):
        doneit = self.search([('done', '=', True)])
        for i in doneit:          
            i.write({'activee': False})
#         changeName="Name Changed"
#         callname=self.browse(67)
#         callname.write({'companyName':changeName})
        return True
#         
#         
        
        
        
        
#     @api.model
#     def search(self, args, offset=0, limit=None, order=None, count=False):
#     
#         if self.companyName:
#             partners = self.env['res.partner']
#         values = partners.distinct_field_get(field='name', value='')
#         return set(values)



#     @api.model
#     def search(self, args, offset=0, limit=None, order=None, count=False):
#         context = self._context or {}
# 
#         if context.get('companyName'):
#             if context.get('type') in ('out_invoice', 'out_refund'):
#                 args += [('type_tax_use', '=', 'sale')]
#             elif context.get('type') in ('in_invoice', 'in_refund'):
#                 args += [('type_tax_use', '=', 'purchase')]
# 
# 
#         return super(carmanumain, self).search(args, offset, limit, order, count=count)
        
#     def browse(self,model):
#                 M = self.pool[model]
#                 # as this method is called before the module update, some xmlid may be invalid at this stage
#                 # explictly filter records before reading them
#                 id = M.exists(self.get(model, []),self)
#                 return M.browse(self)   
        
#     carmanufact.carmanufac(28,)
# 
# 
#     asdf = self.env['student'] student()
#     
#     asasdasdfdf =student.search([('mark','>',35)])  student(11,34,556,)
#     
#     .student.broswe(skarthik) student(karthik,1,2)
#     
#     
#     [()]
#     asdf.search([])


#     
#     a=fields.Monetary(string='Customer price', store=True, readonly=True, compute='_calc_customer_price')#, track_visibility='always'
#     b=fields.Float(string ="in A")
    
    
#     @api.one
#     @api.depends('carmanuPrice')
#     def _calc_customer_price(self,vals):
#         vals['b']=vals['carmanuPrice']
#     check=fie
#     customer_price_amount = fields.Monetary(string='Customer price', store=True, readonly=True, compute='_calc_customer_price', track_visibility='always')
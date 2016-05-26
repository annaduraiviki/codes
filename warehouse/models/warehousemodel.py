from openerp import models, fields, api
 
class warehouse2 (models.Model):
    _name='warehousetab2.warehousetab2'
    
    id=fields.Integer(string="Dbase Id")
    sale = fields.Selection( [('grains',"grains"),('vegetables','vegetables'),('nuts','nuts')], string="Type")
    salename=fields.Char(string="SUB-Type")
    quantity = fields.Integer(string="quantity")
    amount = fields.Float(string="Amount")
    done=fields.Boolean('Done')
    activee=fields.Boolean('Check', default=True )
    doi=fields.Integer(compute='meth', string="DOI")

    
    @api.model
    def create(self,vals):
        if not self.sale:
            vals['sale']='grains'
        res = super(warehouse2, self).create(vals)    
        
        return  res
    
    @api.multi
    def write(self,vals):
        if self.sale=='grains':
            vals['salename'] = 'paddy'
            vals['amount'] = 6 * self.quantity
                            
        res = super(warehouse2, self).write(vals)   
        return res

    @api.one
    def unlink(self):
        if not self.sale:
            print "X"
        return super(warehouse2,self).unlink()
        
    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        default['quantity'] = 20
        res= super(warehouse2, self).copy(default)
        return res
    
    @api.multi
    @api.depends('doi')
    def meth(self):
        self.do_clear_done()
        return
        
        
    @api.multi
    def do_clear_done(self):
        doneit = self.search([('done', '=', True)])
        for i in doneit:
            i.write({'activee': False})
#       changeName="LadiesFinger"    
        callname=self.browse(106)
        callname.write({'salename':'LadiesFinger'})
        return True
#         if self.search([('done','=',True)]):
#             vals['activee'] = False
#             self.activee=False 
           
#         if self.search([('done', '=', True)]):
#              self.write({'activee': False})
#            self.search(['done','=',True])
#            for i in self.done:
#            for i in self.search:
#                i.write({'activee':False})
                
                
           










#    salename = fields.Selection([('paddy','paddy'),('wheat','wheat'),('brinjal','brinjal'),('carrot','carrot'),('pistha','pistha'),('cashew','cashew')],string="item name")
#         if self.sale=='grains' and self.salename=='paddy':
#             vals['salename'] = 'paddy'
#             vals['amount'] = 30 * self.quantity
#         elif self.sale=='grains' and self.salename=='wheat':
#             vals['salename'] = 'wheat'
#             vals['amount'] = 40   * self.quantity 
#         elif self.sale=='vegetables' and self.salename=='brinjal':    
#             vals['salename'] = 'brinjal'
#             vals['amount'] = 10 * self.quantity
#         elif self.sale=='vegetables' and self.salename=='carrot':
#             vals['salename'] = 'carrot'
#             vals['amount']= 50 * self.quantity 
#         elif self.sale=='nuts' and self.salename=='pistha': 
#             vals['salename'] = 'pistha'     
#             vals['amount'] = 20 * self.quantity
#         elif self.sale=='nuts' and self.salename=='cashew':
#             vals['salename']= 'cashew'
#             vals['amount'] = 90 * self.quantity 
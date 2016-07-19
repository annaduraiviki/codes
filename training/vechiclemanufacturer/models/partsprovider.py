from openerp import models, fields, api


class partsproviderclass(models.Model):
    
    _name='partsprovider.vechicle'
    _rec_name='id'

    id=fields.Integer()
    parts_provider=fields.Many2many('supplier.car', string="Parts provider")
    parts_name=fields.Many2many('selection.selection',string="Parts Name")
    parts_price=fields.Float(string="Price of the Part")
    a=fields.Char("Enter to decode")
    encode_value=fields.Char()
    b=fields.Char("decode")        
    
    @api.onchange('a')
    def decode_val(self):
        self.encode_value=self.a.str.decode()
        #self.b.decode=self.encode_value
     
class selectionsxample(models.Model):
    _name='selection.selection'
    _rec_name="name"
    
    name=fields.Char('name',required=True) 
    value=fields.Char('value',required=True)
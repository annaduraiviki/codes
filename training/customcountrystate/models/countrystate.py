from openerp import models,fields,api

class countrystatecode(models.Model):
    _name = 'countrystate.custom'
    _inherits={'basecountry.custom':'state_custom'}
    
    #_inherits={'basecountry.custom':'country_custom'}
    
    #country_custom=fields.Many2one('basecountry.custom',string="Country")
    state_custom=fields.Many2one('basecountry.custom',string="state")
#     state_custom=fields.Char(string="state")
#     area_custom=fields.Char(string="Area")
    
class basecountrycode(models.Model):
    
    _name='basecountry.custom'
    _rec_name='state_base'
    
    country_base=fields.Char(string="Country")
    state_base=fields.Char(string="state")
    area_base=fields.Char(string="Area")
        
    

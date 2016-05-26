# -*- coding: utf-8 -*-

from openerp import models, fields, api

class warehouse2 (models.Model):
    _name='warehousetab2.warehousetab2'
    _inherit='warehousetab2.warehousetab2'
    
    quality=fields.Selection([("g","Good"),("b","Bad"),("a","Average")])

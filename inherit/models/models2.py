# -*- coding: utf-8 -*-

from openerp import models, fields, api

class warehouse (models.Model):
    
    _inherit='warehouse.warehouse'
    
    quality=fields.Selection([("g","Good"),("b","Bad")])

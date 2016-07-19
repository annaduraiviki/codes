from openerp import models,fields,api
import datetime
import time

import datetime
from datetime import timedelta
from datetime import datetime,date
from dateutil.relativedelta import relativedelta 
from dateutil import relativedelta as rdelta
from datetime import date
import time
from datetime import datetime
from datetime import datetime, timedelta

from time import mktime
from datetime import datetime
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT


class mainwindow(models.Model):
    
    _name='window.main'
    _inherit=['customer.car']    
    
    image_window=fields.Binary()
    date_window=fields.Datetime()
    customer_count=fields.Integer(string="Cust. Count")
    servicemen_count=fields.Integer(string="No. of Servicemen")
    regular_customer=fields.Integer(string="Regular cust's")
    
    @api.one
    def date_window_method(self):

            now =datetime.date.today().strftime("%y-%m-%d-%H-%M")
            self.date_window=now 
      
    @api.one
    def cust_count(self):
         
        s=self.env['customer.car'].search_count([])
        self.customer_count=s
        
    @api.one
    def servmen_count(self):
        self.servicemen_count = len(self.env['service.car'].search([]))
  
    @api.one
    def regular_customer_count(self):
        self.regular_customer= len(self.env['customer.car'].search([]))    
        
        
  
  
  
  
  
  
  
  
  
            
            
        
#         for numbofcustomer in self:
#             self.customer_count=numbofcustomer
#             print numbofcustomer
#         return super(mainwindow,self).write()    
            
            
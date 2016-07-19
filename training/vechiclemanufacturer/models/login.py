from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning

class login(models.Model):
    _name='login.vechicle'
    
    user_name=fields.Char(string="User name",required=True,help="This field has ADMIN authenticity, Provide valid user name and password")
    password_login=fields.Char(string="Password",required=True,help="This field has ADMIN authenticity, Provide valid user name and password")
    check_valid=fields.Char(compute="check_user_password",string=" Login",help="If USER NAME and PASSWORD are Matched, Then it will show you LOGIN BUTTON")
    clear_user_password=fields.Char(compute="clear_user_password", string="Clear UserName and Password",help="By clicking this button you can "'Clear'" user name and password ")
    
    
    @api.one
    @api.depends('user_name','password_login')
    def check_user_password(self):    
        if  self.user_name=='vicky' and self.password_login=='vicky':
            self.check_valid=True
            #raise Warning("Login Successful.. Please click ok and proceed..")
#         elif self.user_name==' ' and self.password_login==' ' :
#             raise Warning("Seems Either USER Name or Password are Incorrect.. please check it ")
#         
    @api.one
    @api.depends('user_name','password_login')        
    def clear_user_password(self):
        self.write({'user_name':""})
        self.write({'password_login':""})
            
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
             
        
            #self.check_valid= self.user_name
            
#             
#             if self.check_valid==True:
#                 
#                 return True
#            self.check_valid True

#             return True
#         else:
#             raise Warning("Mismatch error")#             
#             if self.check_valid==True:
#                 
#                 return True
#             
            
        
         
        
        
#         s1= self.search([('user_name','=','anna')])
#         s2= self.search([('password_login','=','anna')])
#          
#         if s1 and s2:
#             self.check_valid
#             res=super(login,self)
#             return res
#         else:
# #          s1 & s2 is False:
#             raise ValidationError("Error")
#              
        
        
        
        
        
                    
            
        
    
    
    
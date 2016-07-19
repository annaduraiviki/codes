from openerp import fields, models

class Partner(models.Model):
    _name='part.samp'
    _inherit = 'customer.car'

    # Add a new column to the res.partner model, by default partners are notname=
    # instructors
    instructor = fields.Boolean("Instructor")

    session_ids = fields.Char( string="Attended Sessions", readonly=True)
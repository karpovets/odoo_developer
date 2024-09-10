from odoo import models, fields

class PersonAbstract(models.AbstractModel):
    _name = 'person.abstract'
    _description = 'Abstract Person Model'
    
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    photo = fields.Binary(string="Photo")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    full_name = fields.Char(string="Full Name", compute='_compute_full_name', readonly=1)

    def _compute_full_name(self):
        for record in self:
            record.full_name = f'{record.first_name} {record.last_name}'

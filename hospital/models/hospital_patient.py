from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Hospital Patient"
    _rec_name = 'full_name'

    full_name = fields.Char(required=1)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    date_of_birth = fields.Date()
    age = fields.Integer()
    passport_data = fields.Char()
    contact_person = fields.Char()
    
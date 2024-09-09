from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Hospital Doctor"
    _rec_name = 'full_name'

    full_name = fields.Char(required=1)
    specialty = fields.Char(required=1)
    
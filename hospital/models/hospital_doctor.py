from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Hospital Doctor"
    _inherit = 'person.abstract'
    _rec_name = 'full_name'

    specialty = fields.Char(required=1)
    
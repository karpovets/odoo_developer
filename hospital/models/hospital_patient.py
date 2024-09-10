from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Hospital Patient"
    _inherit = 'person.abstract'
    _rec_name = 'full_name'

    date_of_birth = fields.Date()
    age = fields.Integer()
    passport_data = fields.Char()
    contact_person_id = fields.Many2one('hospital.contact.person')
    
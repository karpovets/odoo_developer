from odoo import models, fields

class HospitalContactPerson(models.Model):
    _name = 'hospital.contact.person'
    _inherit = 'person.abstract'
    _rec_name = 'full_name'
    

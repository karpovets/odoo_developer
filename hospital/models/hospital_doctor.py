from odoo import models, fields, api
from odoo.exceptions import UserError

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Hospital Doctor"
    _inherit = 'person.abstract'
    _rec_name = 'full_name'

    specialty = fields.Char(required=1)
    intern = fields.Boolean()
    doctor_mentor = fields.Many2one('hospital.doctor', string="Doctor Mentor")

    @api.onchange("doctor_mentor")
    def action_select_doctor_mentor(self):
        if self.doctor_mentor.intern == True:
            raise UserError(('You are not allowed to choose an intern.'))
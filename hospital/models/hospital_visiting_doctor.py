from odoo import models, fields

class HospitalVisitingDoctor(models.Model):
    _name = 'hospital.visiting.doctor'
    _description = "Hospital Visiting Doctor"

    doctor = fields.Many2one('hospital.doctor', required=1)
    patient = fields.Many2one('hospital.patient', required=1)
    visiting_date = fields.Date(required=1)
    diseases = fields.Many2one('hospital.diseases', required=1)
    notes = fields.Text(string="Notes")